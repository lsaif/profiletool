# -*- coding: utf-8 -*-
#-----------------------------------------------------------
#
# Profile
# Copyright (C) 2008  Borys Jurgiel
# Copyright (C) 2012  Patrice Verchere
#-----------------------------------------------------------
#
# licensed under the terms of GNU GPL 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, print to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
#---------------------------------------------------------------------

#Qt import
from qgis.PyQt import uic, QtCore, QtGui
try:
    from qgis.PyQt.QtGui import QWidget
except:
    from qgis.PyQt.QtWidgets import QWidget
from qgis.PyQt.QtSvg import * # required in some distros
#qgis import
import qgis
from qgis.core import *
from qgis.gui import *
#other
import platform
import sys
from math import sqrt
import numpy as np
#plugin import
from .dataReaderTool import DataReaderTool
from .plottingtool import PlottingTool
from .ptmaptool import ProfiletoolMapTool, ProfiletoolMapToolRenderer
from ..ui.ptdockwidget import PTDockWidget

def slopes_pct(p):
    """Return a profile's slope in percentage.

    Returns the x (distance from origin) and y (slope in percentage)
    coordinates for the plot.
    """
    x = np.array(p["l"])
    y = np.array(p["z"])
    slope_pct = 100 * (y[1:]-y[:-1])/(x[1:]-x[:-1])
    slope_pct[np.isnan(slope_pct)] = 0
    slope_pct[np.isinf(slope_pct)] = 0
    px = 0.5*(x[:-1]+x[1:])
    return px, slope_pct

def slopes_deg(p):
    x, slope_pct = slopes_pct(p)
    slope_deg = np.degrees(np.arctan(slope_pct/100.0))
    return x, slope_deg

class ProfileToolCore(QWidget):


    plot_profiles = {u"Height": lambda p: (p["l"], p["z"]),
                     u"Slope (%)": slopes_pct,
                     u"Slope (°)": slopes_deg}
    def __init__(self, iface,plugincore, parent = None):
        QWidget.__init__(self, parent)
        self.iface = iface
        self.plugincore = plugincore

        #remimber repository for saving
        if QtCore.QSettings().value("profiletool/lastdirectory") != '':
            self.loaddirectory = QtCore.QSettings().value("profiletool/lastdirectory")
        else:
            self.loaddirectory = ''


        #mouse tracking
        self.doTracking = False
        #the datas / results
        self.profiles = None        #dictionary where is saved the plotting data {"l":[l],"z":[z], "layer":layer1, "curve":curve1}
        #The line information
        self.pointstoDraw = None
        #he renderer for temporary polyline
        #self.toolrenderer = ProfiletoolMapToolRenderer(self)
        self.toolrenderer = None
        #the maptool previously loaded
        self.saveTool = None                #Save the standard mapttool for restoring it at the end
        # Used to remove highlighting from previously active layer.
        self.previousLayer = None
        self.x_cursor = None    # Keep track of last x position of cursor
        #the dockwidget
        self.dockwidget = PTDockWidget(self.iface,self)
        # Initialize the combo box with the list of available profiles.
        # (Use sorted list to be sure that Height is always on top and
        # the combobox order is consistent)
        for profile in sorted(self.plot_profiles):
            self.dockwidget.plotComboBox.addItem(profile)
        self.dockwidget.plotComboBox.setCurrentIndex(0)
        self.dockwidget.plotComboBox.currentIndexChanged.connect(
            lambda index: self.plotProfil())
        #dockwidget graph zone
        self.dockwidget.changePlotLibrary( self.dockwidget.cboLibrary.currentIndex() )


    def activateProfileMapTool(self):
        self.saveTool = self.iface.mapCanvas().mapTool()            #Save the standard mapttool for restoring it at the end
        #Listeners of mouse
        self.toolrenderer = ProfiletoolMapToolRenderer(self)
        self.toolrenderer.connectTool()
        self.toolrenderer.setSelectionMethod(
                self.dockwidget.comboBox.currentIndex())
        #init the mouse listener comportement and save the classic to restore it on quit
        self.iface.mapCanvas().setMapTool(self.toolrenderer.tool)



    #******************************************************************************************
    #**************************** function part *************************************************
    #******************************************************************************************


    def updateProfilFromFeatures(self, layer, features):
        """Updates self.profiles from given feature list.

        This function extracts the list of coordinates from the given
        feature set and calls updateProfil.
        This function also manages selection/deselection of features in the
        active layer to highlight the feature being profiled.
        """
        pointstoDraw = []
        if self.previousLayer:
            # Be sure that we unselect anything in the previous layer.
            self.previousLayer.removeSelection()
        self.previousLayer = layer

        if layer:
            layer.removeSelection()
            layer.select([f.id() for f in features])
            for feature in features:
                k = 0
                while not feature.geometry().vertexAt(k) == QgsPoint(0,0):
                    point2 = self.toolrenderer.tool.toMapCoordinates(
                            layer, 
                            QgsPointXY(feature.geometry().vertexAt(k)))
                    pointstoDraw += [[point2.x(),point2.y()]]
                    k += 1

        self.updateProfil(pointstoDraw, False)

    def updateProfil(self, points1, removeSelection=True):
        """Updates self.profiles from values in points1.

        This function can be called from updateProfilFromFeatures or from
        ProfiletoolMapToolRenderer (with a list of points from rubberband).
        """
        if removeSelection and self.previousLayer:
            # Be sure that we unselect anything in the previous layer.
            self.previousLayer.removeSelection()
        # replicate last point (bug #6680)
        if points1:
            points1 = points1 + [points1[-1]]
        self.pointstoDraw = points1
        self.profiles = []

        profile_func = self.plot_profiles[
                            self.dockwidget.plotComboBox.currentText()]
        #calculate profiles
        for i in range(0 , self.dockwidget.mdl.rowCount()):
            self.profiles.append( {"layer": self.dockwidget.mdl.item(i,5).data(QtCore.Qt.EditRole) } )
            self.profiles[i]["band"] = self.dockwidget.mdl.item(i,3).data(QtCore.Qt.EditRole)
            #if self.dockwidget.mdl.item(i,5).data(Qt.EditRole).type() == self.dockwidget.mdl.item(i,5).data(Qt.EditRole).VectorLayer :
            if self.dockwidget.mdl.item(i,5).data(QtCore.Qt.EditRole).type() == qgis.core.QgsMapLayer.VectorLayer :
                self.profiles[i], _, _ = DataReaderTool().dataVectorReaderTool(self.iface, self.toolrenderer.tool, self.profiles[i], self.pointstoDraw, float(self.dockwidget.mdl.item(i,4).data(QtCore.Qt.EditRole)) )
            else:
                self.profiles[i] = DataReaderTool().dataRasterReaderTool(self.iface, self.toolrenderer.tool, self.profiles[i], self.pointstoDraw, self.dockwidget.checkBox.isChecked())
            self.profiles[i]["plot_x"], self.profiles[i]["plot_y"] = \
                profile_func(self.profiles[i])
        self.plotProfil()

    def plotProfil(self, vertline = True):
        self.disableMouseCoordonates()

        self.removeClosedLayers(self.dockwidget.mdl)
        PlottingTool().clearData(self.dockwidget, self.profiles, self.dockwidget.plotlibrary)

        if not self.pointstoDraw:
            return

        if vertline:                        #Plotting vertical lines at the node of polyline draw
            PlottingTool().drawVertLine(self.dockwidget, self.pointstoDraw, self.dockwidget.plotlibrary)

        #calculate buffer geometries if search buffer is set in mdt layer
        geoms = []
        for i in range(0 , self.dockwidget.mdl.rowCount()):
            #if self.dockwidget.mdl.item(i,5).data(Qt.EditRole).type() == self.dockwidget.mdl.item(i,5).data(Qt.EditRole).VectorLayer :
            if self.dockwidget.mdl.item(i,5).data(QtCore.Qt.EditRole).type() == qgis.core.QgsMapLayer.VectorLayer :
                _, buffer, multipoly = DataReaderTool().dataVectorReaderTool(self.iface, self.toolrenderer.tool, self.profiles[i], self.pointstoDraw, float(self.dockwidget.mdl.item(i,4).data(QtCore.Qt.EditRole)) )
                geoms.append(buffer)
                geoms.append(multipoly)
        self.toolrenderer.setBufferGeometry(geoms)

        # Update coordinates to use in plot (height, slope %...)
        profile_func = self.plot_profiles[
                            self.dockwidget.plotComboBox.currentText()]

        for i in range(0 , self.dockwidget.mdl.rowCount()):
            self.profiles[i]["plot_x"], self.profiles[i]["plot_y"] = \
                profile_func(self.profiles[i])

        #plot profiles
        PlottingTool().attachCurves(self.dockwidget, self.profiles, self.dockwidget.mdl, self.dockwidget.plotlibrary)
        PlottingTool().reScalePlot(self.dockwidget, self.profiles, self.dockwidget.plotlibrary)
        #create tab with profile xy
        self.dockwidget.updateCoordinateTab()
        #Mouse tracking


        self.updateCursorOnMap(self.x_cursor)
        self.enableMouseCoordonates(self.dockwidget.plotlibrary)

    def updateCursorOnMap(self, x):
        self.x_cursor = x
        if self.pointstoDraw and self.doTracking:
            self.toolrenderer.rubberbandpoint.show()
            if x is not None:
                points = [QgsPoint(p[0], p[1]) for p in self.pointstoDraw]
                geom =  qgis.core.QgsGeometry.fromPolyline(points)
                pointprojected = geom.interpolate(x)

                self.toolrenderer.rubberbandpoint.setCenter(
                        pointprojected.asPoint())
        else:
            self.toolrenderer.rubberbandpoint.hide()

    # remove layers which were removed from QGIS
    def removeClosedLayers(self, model1):
        qgisLayerNames = []
        if int(QtCore.QT_VERSION_STR[0]) == 4 :    #qgis2
            qgisLayerNames = [  layer.name()    for layer in self.iface.legendInterface().layers()]
            """
            for i in range(0, self.iface.mapCanvas().layerCount()):
                    qgisLayerNames.append(self.iface.mapCanvas().layer(i).name())
            """
        elif int(QtCore.QT_VERSION_STR[0]) == 5 :    #qgis3
            qgisLayerNames = [  layer.name()    for layer in qgis.core.QgsProject().instance().mapLayers().values()]

        #print('qgisLayerNames',qgisLayerNames)
        for i in range(0 , model1.rowCount()):
            layerName = model1.item(i,2).data(QtCore.Qt.EditRole)
            if not layerName in qgisLayerNames:
                self.dockwidget.removeLayer(i)
                self.removeClosedLayers(model1)
                break

    def cleaning(self):
        self.updateProfilFromFeatures(None, [])
        if self.toolrenderer:
            self.toolrenderer.cleaning()


    #******************************************************************************************
    #**************************** mouse interaction *******************************************
    #******************************************************************************************

    def activateMouseTracking(self,int1):

        if self.dockwidget.TYPE == 'PyQtGraph':

            if int1 == 2 :
                self.doTracking = True
            elif int1 == 0 :
                self.doTracking = False

        elif self.dockwidget.TYPE == 'Matplotlib':
            if int1 == 2 :
                self.doTracking = True
                self.cid = self.dockwidget.plotWdg.mpl_connect('motion_notify_event', self.mouseevent_mpl)
            elif int1 == 0 :
                self.doTracking = False
                try:
                    self.dockwidget.plotWdg.mpl_disconnect(self.cid)
                except:
                    pass
                try:
                    if self.vline:
                        self.dockwidget.plotWdg.figure.get_axes()[0].lines.remove(self.vline)
                        self.dockwidget.plotWdg.draw()
                except Exception as e:
                    print(str(e) )



    def mouseevent_mpl(self,event):
        """
        case matplotlib library
        """
        if event.xdata:
            try:
                if self.vline:
                    self.dockwidget.plotWdg.figure.get_axes()[0].lines.remove(self.vline)
            except Exception as e:
                pass
            xdata = float(event.xdata)
            self.vline = self.dockwidget.plotWdg.figure.get_axes()[0].axvline(xdata,linewidth=2, color = 'k')
            self.dockwidget.plotWdg.draw()
            """
            i=1
            while  i < len(self.tabmouseevent) and xdata > self.tabmouseevent[i][0] :
                i=i+1
            i=i-1
            x = self.tabmouseevent[i][1] +(self.tabmouseevent[i+1][1] - self.tabmouseevent[i][1] )/ ( self.tabmouseevent[i+1][0] - self.tabmouseevent[i][0]  )  *   (xdata - self.tabmouseevent[i][0])
            y = self.tabmouseevent[i][2] +(self.tabmouseevent[i+1][2] - self.tabmouseevent[i][2] )/ ( self.tabmouseevent[i+1][0] - self.tabmouseevent[i][0]  )  *   (xdata - self.tabmouseevent[i][0])
            self.toolrenderer.rubberbandpoint.show()
            point = QgsPoint( x,y )
            self.toolrenderer.rubberbandpoint.setCenter(point)
            """
            self.updateCursorOnMap(xdata)


    def enableMouseCoordonates(self,library):
        if library == "PyQtGraph":
            self.dockwidget.plotWdg.scene().sigMouseMoved.connect(self.mouseMovedPyQtGraph)
            self.dockwidget.plotWdg.getViewBox().autoRange( items=self.dockwidget.plotWdg.getPlotItem().listDataItems())
            #self.dockwidget.plotWdg.getViewBox().sigRangeChanged.connect(self.dockwidget.plotRangechanged)
            self.dockwidget.connectPlotRangechanged()



    def disableMouseCoordonates(self):
        try:
            self.dockwidget.plotWdg.scene().sigMouseMoved.disconnect(self.mouseMovedPyQtGraph)
        except:
            pass

        self.dockwidget.disconnectPlotRangechanged()



    def mouseMovedPyQtGraph(self, pos): # si connexion directe du signal "mouseMoved" : la fonction reçoit le point courant
            roundvalue = 3

            if self.dockwidget.plotWdg.sceneBoundingRect().contains(pos): # si le point est dans la zone courante

                if self.dockwidget.showcursor :
                    range = self.dockwidget.plotWdg.getViewBox().viewRange()
                    mousePoint = self.dockwidget.plotWdg.getViewBox().mapSceneToView(pos) # récupère le point souris à partir ViewBox

                    datas = []
                    pitems = self.dockwidget.plotWdg.getPlotItem()
                    ytoplot = None
                    xtoplot = None

                    if len(pitems.listDataItems())>0:
                        #get data and nearest xy from cursor
                        compt = 0
                        for  item in pitems.listDataItems():
                            if item.isVisible() :
                                x,y = item.getData()
                                nearestindex = np.argmin( abs(np.array(x)-mousePoint.x()) )
                                if compt == 0:
                                    xtoplot = np.array(x)[nearestindex]
                                    ytoplot = np.array(y)[nearestindex]
                                else:
                                    if abs( np.array(y)[nearestindex] - mousePoint.y() ) < abs( ytoplot -  mousePoint.y() ):
                                        ytoplot = np.array(y)[nearestindex]
                                        xtoplot = np.array(x)[nearestindex]
                                compt += 1
                        #plot xy label and cursor
                        if not xtoplot is None and not ytoplot is None:
                            for item in self.dockwidget.plotWdg.allChildItems():
                                if str(type(item)) == "<class 'profiletool.pyqtgraph.graphicsItems.InfiniteLine.InfiniteLine'>":
                                    if item.name() == 'cross_vertical':
                                        item.show()
                                        item.setPos(xtoplot)
                                    elif item.name() == 'cross_horizontal':
                                        item.show()
                                        item.setPos(ytoplot)
                                elif str(type(item)) == "<class 'profiletool.pyqtgraph.graphicsItems.TextItem.TextItem'>":
                                    if item.textItem.toPlainText()[0] == 'X':
                                        item.show()
                                        item.setText('X : '+str(round(xtoplot,roundvalue)))
                                        item.setPos(xtoplot,range[1][0] )
                                    elif item.textItem.toPlainText()[0] == 'Y':
                                        item.show()
                                        item.setText('Y : '+str(round(ytoplot,roundvalue)))
                                        item.setPos(range[0][0],ytoplot )
                    #tracking part
                    self.updateCursorOnMap(xtoplot)
