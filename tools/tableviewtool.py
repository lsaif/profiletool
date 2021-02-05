# -*- coding: utf-8 -*-
#-----------------------------------------------------------
#
# Profile
# Copyright (C) 2012  Patrice Verchere
# Copyright (C) 2021  Luthfi Saifudin
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
# with this progsram; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
#---------------------------------------------------------------------
#Qt import
from qgis.PyQt import uic, QtCore, QtGui
try:
    from qgis.PyQt.QtGui import QInputDialog, QMessageBox
except:
    from qgis.PyQt.QtWidgets import QInputDialog, QMessageBox
#qgis import
from qgis.core import *
from qgis.gui import *
#plugin import
from .plottingtool import *
from .utils import isProfilable


class TableViewTool(QtCore.QObject):

    layerAddedOrRemoved = QtCore.pyqtSignal() # Emitted when a new layer is added

    def addLayer(self , iface, mdl, layer1 = None):
        if layer1 is None:
            templist=[]
            j=0
            # Ask the layer by a input dialog
            for i in range(0, iface.mapCanvas().layerCount()):
                donothing = False
                layer = iface.mapCanvas().layer(i)
                if isProfilable(layer):
                    for j in range(0, mdl.rowCount()):
                        if str(mdl.item(j,2).data(QtCore.Qt.EditRole)) == str(layer.name()):
                            donothing = True
                else:
                    donothing = True

                if donothing == False:
                    templist +=  [[layer, layer.name()]]

            if len(templist) == 0:
                QMessageBox.warning(iface.mainWindow(), "Profile tool", "No raster to add")
                return
            else:
                testqt, ok = QInputDialog.getItem(iface.mainWindow(), "Layer selector", "Choose layer", [templist[k][1] for k in range( len(templist) )], False)
                if ok:
                    for i in range (0,len(templist)):
                        if templist[i][1] == testqt:
                            layer2 = templist[i][0]
                else:
                    return
        else :
            if isProfilable(layer1):
                layer2 = layer1
            else:
                text = "Active layer is not a profilable layer."
                if layer1.type() == layer1.MeshLayer:
                    text +="\n(MeshLayer support requires QGis version 3.6 or newer.)"
                QMessageBox.warning(iface.mainWindow(), "Profile tool", text)
                return

        # Ask the Band by a input dialog
        #First, if isProfilable, considerate the real band number (instead of band + 1 for raster)
        if layer2.type() == layer2.PluginLayer and  isProfilable(layer2) or \
           layer2.type() == layer2.MeshLayer:
            self.bandoffset = 0
            typename = 'parameter'
        elif layer2.type() == layer2.RasterLayer:
            self.bandoffset = 1
            typename = 'band'
        elif layer2.type() == layer2.VectorLayer:
            self.bandoffset = 0
            typename = 'field'


        if layer2.type() == layer2.RasterLayer and layer2.bandCount() != 1:
            listband = []
            for i in range(0,layer2.bandCount()):
                listband.append(str(i+self.bandoffset))
            testqt, ok = QInputDialog.getItem(
                iface.mainWindow(),
                typename.capitalize() + " selector",
                "Choose the " + typename,
                listband,
                False)
            if ok :
                choosenBand = int(testqt) - self.bandoffset
            else:
                return 2
        elif layer2.type() == layer2.VectorLayer :
            fieldstemp = [field.name() for field in layer2.fields() ]
            if int(QtCore.QT_VERSION_STR[0]) == 4 :    #qgis2
                fields = [field.name() for field in layer2.fields() if field.type() in [2,3,4,5,6]]

            elif int(QtCore.QT_VERSION_STR[0]) == 5 :    #qgis3
                fields = [field.name() for field in layer2.fields() if field.isNumeric()]
            if len(fields)==0:
                QMessageBox.warning(iface.mainWindow(), "Profile tool", "Active layer is not a profilable layer")
                return
            elif len(fields) == 1 :
                choosenBand = fieldstemp.index(fields[0])

            else:
                try:
                    defaultfield = fieldstemp.index('z')
                except ValueError:
                    defaultfield = 2
                testqt, ok = QInputDialog.getItem(
                    iface.mainWindow(),
                    typename.capitalize() + " selector",
                    "Choose the " + typename,
                    fields,
                    defaultfield)
                if ok:
                    choosenBand = fieldstemp.index(testqt)
                else:
                    return defaultfield

        else:
            choosenBand = 0

        #Complete the tableview
        row = mdl.rowCount()
        mdl.insertRow(row)
        mdl.setData(mdl.index(row, 0, QModelIndex())  ,True, QtCore.Qt.CheckStateRole)
        mdl.item(row,0).setFlags(QtCore.Qt.ItemIsSelectable)
        lineColour = QtCore.Qt.red
        #QGis2
        if layer2.type() == layer2.PluginLayer and layer2.LAYER_TYPE == 'crayfish_viewer' or \
           layer2.type() == layer2.MeshLayer:    #QGis3
            lineColour = QtCore.Qt.blue
        mdl.setData( mdl.index(row, 1, QModelIndex())  ,QColor(lineColour) , QtCore.Qt.BackgroundRole)
        mdl.item(row,1).setFlags(QtCore.Qt.NoItemFlags)
        mdl.setData( mdl.index(row, 2, QModelIndex())  ,layer2.name())
        mdl.item(row,2).setFlags(QtCore.Qt.NoItemFlags)
        mdl.setData( mdl.index(row, 3, QModelIndex())  ,choosenBand + self.bandoffset)
        mdl.item(row,3).setFlags(QtCore.Qt.NoItemFlags)

        if layer2.type() == layer2.VectorLayer :
            #mdl.setData( mdl.index(row, 4, QModelIndex())  ,QVariant(100.0))
            mdl.setData(mdl.index(row, 4, QModelIndex()), 3.0)
            '''listPlotTypes = ['Line','Point']
            i = mdl.index(row, 5)
            plotTypes = QComboBox()
            pix = QPersistentModelIndex(i)
            plotTypes.currentIndexChanged[str].connect(lambda txt, pix=pix:mdl.setData(QModelIndex(pix), txt))
            plotTypes.addItems(listPlotTypes)
            self.tableview.setIndexWidget(i, plotTypes)
            sizeOptions = QComboBox()
            listSize = listband.append('')
            sizeOptions.addItems(listSize)
            sizeOptions.setCurrentIndex(listSize.index(0))
            mdl.setData(mdl.index(row, 6, QModelIndex()), sizeOptions)
            listband = []
            for i in range(0,layer2.bandCount()):
                listband.append(str(i+self.bandoffset))
            colorOptions = QComboBox()
            listColor = listband.append('')
            colorOptions.addItems(listSize)
            colorOptions.setCurrentIndex(listColor.index(0))
            mdl.setData(mdl.index(row, 6, QModelIndex()), colorOptions)
            mdl.setData(mdl.index(row, 7, QModelIndex()), colorOptions)'''
            #mdl.item(row,3).setFlags(Qt.NoItemFlags)
            mdl.setData(mdl.index(row, 5, QModelIndex()), 'Line')
            mdl.setData(mdl.index(row, 6, QModelIndex()), 'Standard')
            mdl.setData(mdl.index(row, 7, QModelIndex()), 'Selected')
            
        else:
            mdl.setData(mdl.index(row, 4, QModelIndex()), '')
            mdl.item(row,4).setFlags(QtCore.Qt.NoItemFlags)
            mdl.setData(mdl.index(row, 5, QModelIndex()), '')
            mdl.item(row,5).setFlags(QtCore.Qt.NoItemFlags)
            mdl.setData(mdl.index(row, 6, QModelIndex()), '')
            mdl.item(row,6).setFlags(QtCore.Qt.NoItemFlags)
            mdl.setData(mdl.index(row, 7, QModelIndex()), '')
            mdl.item(row,7).setFlags(QtCore.Qt.NoItemFlags)


        mdl.setData( mdl.index(row, 8, QModelIndex())  ,layer2)
        mdl.item(row,8).setFlags(QtCore.Qt.NoItemFlags)
        self.layerAddedOrRemoved.emit()


    def removeLayer(self, mdl, index):
            try:
                mdl.removeRow(index)
                self.layerAddedOrRemoved.emit()
            except:
                return

    def chooseLayerForRemoval(self, iface, mdl):

        if mdl.rowCount() < 2:
            if mdl.rowCount() == 1:
                return 0
            return None

        list1 = []
        for i in range(0,mdl.rowCount()):
            list1.append(str(i +1) + " : " + mdl.item(i,2).data(QtCore.Qt.EditRole))
        testqt, ok = QInputDialog.getItem(iface.mainWindow(), "Layer selector", "Choose the Layer", list1, False)
        if ok:
            for i in range(0,mdl.rowCount()):
                if testqt == (str(i+1) + " : " + mdl.item(i,2).data(QtCore.Qt.EditRole)):
                    return i
        return None

    def onClick(self, iface, wdg, mdl, plotlibrary, index1):                    #action when clicking the tableview
        temp = mdl.itemFromIndex(index1)
        layer = mdl.index(index1.row(),8).data()
        if index1.column() == 1:                #modifying color
            name = ("%s#%d") % (mdl.item(index1.row(),2).data(QtCore.Qt.EditRole), mdl.item(index1.row(),3).data(QtCore.Qt.EditRole))
            color = QColorDialog().getColor(temp.data(QtCore.Qt.BackgroundRole))
            mdl.setData( mdl.index(temp.row(), 1, QModelIndex())  ,color , QtCore.Qt.BackgroundRole)
            mdl.setData(mdl.index(temp.row(), 7, QModelIndex()), 'Selected')
            PlottingTool().changeColor(wdg, plotlibrary, mdl, color, name)
        elif index1.column() == 0:                #modifying checkbox
            #name = mdl.item(index1.row(),2).data(Qt.EditRole)
            name = ("%s#%d") % (mdl.item(index1.row(),2).data(QtCore.Qt.EditRole), mdl.item(index1.row(),3).data(QtCore.Qt.EditRole))
            booltemp = temp.data(QtCore.Qt.CheckStateRole)
            if booltemp == True:
                booltemp = False
            else:
                booltemp = True
            mdl.setData( mdl.index(temp.row(), 0, QModelIndex())  ,booltemp, QtCore.Qt.CheckStateRole)
            PlottingTool().changeAttachCurve(wdg, plotlibrary, booltemp, name)
        elif index1.column() == 5:                
            name = ("%s#%d") % (mdl.item(index1.row(),2).data(QtCore.Qt.EditRole), mdl.item(index1.row(),3).data(QtCore.Qt.EditRole))
            linetype = mdl.index(index1.row(),5).data()
            flags = mdl.item(index1.row(),6).flags()
            if linetype == 'Line':
                linetype = 'Point'
                mdl.item(temp.row(),6).setFlags(mdl.item(temp.row(),6).flags() ^ QtCore.Qt.NoItemFlags)
                mdl.item(temp.row(),7).setFlags(mdl.item(temp.row(),7).flags() ^ QtCore.Qt.NoItemFlags)
            else:
                linetype = 'Line'
                flags = QtCore.Qt.NoItemFlags
                mdl.setData(mdl.index(temp.row(), 6, QModelIndex()), 'Standard')
                mdl.setData(mdl.index(temp.row(), 7, QModelIndex()), 'Selected')
            mdl.setData(mdl.index(temp.row(), 5, QModelIndex()), linetype)
            PlottingTool().changeDataPlot(wdg, plotlibrary, mdl, linetype, name)
        elif index1.column() == 6:  
            name = ("%s#%d") % (mdl.item(index1.row(),2).data(QtCore.Qt.EditRole), mdl.item(index1.row(),3).data(QtCore.Qt.EditRole))
            dotSize = mdl.index(index1.row(),6).data()
            linetype = mdl.index(index1.row(),5).data()
            if (dotSize == 'Standard') & (linetype == 'Point'):
                dotSize = 'As Layer'
            else:
                dotSize = 'Standard'
            mdl.setData(mdl.index(temp.row(), 6, QModelIndex()), dotSize)
            PlottingTool().changeDataPlotSize(wdg, plotlibrary, mdl, layer, dotSize, name)
        elif index1.column() == 7:  
            name = ("%s#%d") % (mdl.item(index1.row(),2).data(QtCore.Qt.EditRole), mdl.item(index1.row(),3).data(QtCore.Qt.EditRole))
            dotColor = mdl.index(index1.row(),7).data()
            linetype = mdl.index(index1.row(),5).data()
            if (dotColor == 'Selected') & (linetype == 'Point'):
                dotColor = 'As Layer'
            else:
                dotColor = 'Selected'
            mdl.setData(mdl.index(temp.row(), 7, QModelIndex()), dotColor)
            PlottingTool().changeDataPlotColor(wdg, plotlibrary, mdl, layer, dotColor, name)
        elif False and index1.column() == 8:
            #name = mdl.item(index1.row(),2).data(Qt.EditRole)
            name = mdl.item(index1.row(),8).data(QtCore.Qt.EditRole)
            print(name)

        else:
            return
