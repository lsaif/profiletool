# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profilebase.ui'
#
# Created: Sat Mar 10 08:03:33 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ProfileBase(object):
    def setupUi(self, ProfileBase):
        ProfileBase.setObjectName(_fromUtf8("ProfileBase"))
        ProfileBase.resize(724, 358)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProfileBase.sizePolicy().hasHeightForWidth())
        ProfileBase.setSizePolicy(sizePolicy)
        ProfileBase.setFocusPolicy(QtCore.Qt.NoFocus)
        ProfileBase.setWindowTitle(QtGui.QApplication.translate("ProfileBase", "Profile", None, QtGui.QApplication.UnicodeUTF8))
        ProfileBase.setSizeGripEnabled(True)
        self.gridlayout = QtGui.QGridLayout(ProfileBase)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.tabWidget = QtGui.QTabWidget(ProfileBase)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridlayout1 = QtGui.QGridLayout(self.tab)
        self.gridlayout1.setObjectName(_fromUtf8("gridlayout1"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.scaleSlider = QtGui.QSlider(self.tab)
        self.scaleSlider.setOrientation(QtCore.Qt.Vertical)
        self.scaleSlider.setObjectName(_fromUtf8("scaleSlider"))
        self.hboxlayout.addWidget(self.scaleSlider)
        self.qwtPlot = QwtPlot(self.tab)
        self.qwtPlot.setAutoFillBackground(False)
        self.qwtPlot.setObjectName(_fromUtf8("qwtPlot"))
        self.hboxlayout.addWidget(self.qwtPlot)
        self.gridlayout1.addLayout(self.hboxlayout, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.vboxlayout = QtGui.QVBoxLayout(self.tab_2)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        self.statBox1 = QtGui.QGroupBox(self.tab_2)
        self.statBox1.setTitle(QtGui.QApplication.translate("ProfileBase", "Profile 1", None, QtGui.QApplication.UnicodeUTF8))
        self.statBox1.setObjectName(_fromUtf8("statBox1"))
        self.gridlayout2 = QtGui.QGridLayout(self.statBox1)
        self.gridlayout2.setObjectName(_fromUtf8("gridlayout2"))
        self.stat1 = QtGui.QLabel(self.statBox1)
        self.stat1.setText(QtGui.QApplication.translate("ProfileBase", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.stat1.setTextFormat(QtCore.Qt.AutoText)
        self.stat1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.stat1.setWordWrap(True)
        self.stat1.setObjectName(_fromUtf8("stat1"))
        self.gridlayout2.addWidget(self.stat1, 0, 0, 1, 1)
        self.hboxlayout1.addWidget(self.statBox1)
        self.statBox2 = QtGui.QGroupBox(self.tab_2)
        self.statBox2.setTitle(QtGui.QApplication.translate("ProfileBase", "Profile 2", None, QtGui.QApplication.UnicodeUTF8))
        self.statBox2.setObjectName(_fromUtf8("statBox2"))
        self.gridlayout3 = QtGui.QGridLayout(self.statBox2)
        self.gridlayout3.setObjectName(_fromUtf8("gridlayout3"))
        self.stat2 = QtGui.QLabel(self.statBox2)
        self.stat2.setText(QtGui.QApplication.translate("ProfileBase", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.stat2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.stat2.setWordWrap(True)
        self.stat2.setObjectName(_fromUtf8("stat2"))
        self.gridlayout3.addWidget(self.stat2, 0, 0, 1, 1)
        self.hboxlayout1.addWidget(self.statBox2)
        self.statBox3 = QtGui.QGroupBox(self.tab_2)
        self.statBox3.setTitle(QtGui.QApplication.translate("ProfileBase", "Profile 3", None, QtGui.QApplication.UnicodeUTF8))
        self.statBox3.setObjectName(_fromUtf8("statBox3"))
        self.gridlayout4 = QtGui.QGridLayout(self.statBox3)
        self.gridlayout4.setObjectName(_fromUtf8("gridlayout4"))
        self.stat3 = QtGui.QLabel(self.statBox3)
        self.stat3.setText(QtGui.QApplication.translate("ProfileBase", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.stat3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.stat3.setWordWrap(True)
        self.stat3.setObjectName(_fromUtf8("stat3"))
        self.gridlayout4.addWidget(self.stat3, 0, 0, 1, 1)
        self.hboxlayout1.addWidget(self.statBox3)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.groupBox = QtGui.QGroupBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 90))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox.setTitle(QtGui.QApplication.translate("ProfileBase", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridlayout5 = QtGui.QGridLayout(self.groupBox)
        self.gridlayout5.setObjectName(_fromUtf8("gridlayout5"))
        self.stats = QtGui.QLabel(self.groupBox)
        self.stats.setText(QtGui.QApplication.translate("ProfileBase", "Start\n"
"Stop\n"
"Length", None, QtGui.QApplication.UnicodeUTF8))
        self.stats.setTextFormat(QtCore.Qt.AutoText)
        self.stats.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.stats.setWordWrap(True)
        self.stats.setObjectName(_fromUtf8("stats"))
        self.gridlayout5.addWidget(self.stats, 0, 0, 1, 1)
        self.vboxlayout.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.gridlayout6 = QtGui.QGridLayout(self.tab_4)
        self.gridlayout6.setObjectName(_fromUtf8("gridlayout6"))
        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setObjectName(_fromUtf8("hboxlayout2"))
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.label_23 = QtGui.QLabel(self.tab_4)
        self.label_23.setText(QtGui.QApplication.translate("ProfileBase", "Profile 1:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.vboxlayout1.addWidget(self.label_23)
        self.setLayer1 = QtGui.QComboBox(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setLayer1.sizePolicy().hasHeightForWidth())
        self.setLayer1.setSizePolicy(sizePolicy)
        self.setLayer1.setObjectName(_fromUtf8("setLayer1"))
        self.vboxlayout1.addWidget(self.setLayer1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.vboxlayout1.addItem(spacerItem)
        self.hboxlayout2.addLayout(self.vboxlayout1)
        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setObjectName(_fromUtf8("hboxlayout3"))
        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setObjectName(_fromUtf8("vboxlayout2"))
        self.label_24 = QtGui.QLabel(self.tab_4)
        self.label_24.setText(QtGui.QApplication.translate("ProfileBase", "R", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.vboxlayout2.addWidget(self.label_24)
        self.label_25 = QtGui.QLabel(self.tab_4)
        self.label_25.setText(QtGui.QApplication.translate("ProfileBase", "G", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.vboxlayout2.addWidget(self.label_25)
        self.label_26 = QtGui.QLabel(self.tab_4)
        self.label_26.setText(QtGui.QApplication.translate("ProfileBase", "B", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.vboxlayout2.addWidget(self.label_26)
        self.hboxlayout3.addLayout(self.vboxlayout2)
        self.vboxlayout3 = QtGui.QVBoxLayout()
        self.vboxlayout3.setObjectName(_fromUtf8("vboxlayout3"))
        self.setR1 = QtGui.QSlider(self.tab_4)
        self.setR1.setMinimumSize(QtCore.QSize(35, 0))
        self.setR1.setMaximumSize(QtCore.QSize(200, 16777215))
        self.setR1.setOrientation(QtCore.Qt.Horizontal)
        self.setR1.setObjectName(_fromUtf8("setR1"))
        self.vboxlayout3.addWidget(self.setR1)
        self.setG1 = QtGui.QSlider(self.tab_4)
        self.setG1.setMaximumSize(QtCore.QSize(200, 16777215))
        self.setG1.setOrientation(QtCore.Qt.Horizontal)
        self.setG1.setObjectName(_fromUtf8("setG1"))
        self.vboxlayout3.addWidget(self.setG1)
        self.setB1 = QtGui.QSlider(self.tab_4)
        self.setB1.setMaximumSize(QtCore.QSize(200, 16777215))
        self.setB1.setOrientation(QtCore.Qt.Horizontal)
        self.setB1.setObjectName(_fromUtf8("setB1"))
        self.vboxlayout3.addWidget(self.setB1)
        self.hboxlayout3.addLayout(self.vboxlayout3)
        self.colorBox1 = QtGui.QGraphicsView(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorBox1.sizePolicy().hasHeightForWidth())
        self.colorBox1.setSizePolicy(sizePolicy)
        self.colorBox1.setMaximumSize(QtCore.QSize(50, 50))
        self.colorBox1.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.colorBox1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.colorBox1.setAcceptDrops(False)
        self.colorBox1.setAutoFillBackground(True)
        self.colorBox1.setInteractive(False)
        self.colorBox1.setTransformationAnchor(QtGui.QGraphicsView.NoAnchor)
        self.colorBox1.setViewportUpdateMode(QtGui.QGraphicsView.FullViewportUpdate)
        self.colorBox1.setOptimizationFlags(QtGui.QGraphicsView.DontClipPainter)
        self.colorBox1.setObjectName(_fromUtf8("colorBox1"))
        self.hboxlayout3.addWidget(self.colorBox1)
        self.hboxlayout2.addLayout(self.hboxlayout3)
        self.gridlayout6.addLayout(self.hboxlayout2, 0, 0, 1, 1)
        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setObjectName(_fromUtf8("hboxlayout4"))
        self.vboxlayout4 = QtGui.QVBoxLayout()
        self.vboxlayout4.setObjectName(_fromUtf8("vboxlayout4"))
        self.label_28 = QtGui.QLabel(self.tab_4)
        self.label_28.setText(QtGui.QApplication.translate("ProfileBase", "Profile 2:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.vboxlayout4.addWidget(self.label_28)
        self.setLayer2 = QtGui.QComboBox(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setLayer2.sizePolicy().hasHeightForWidth())
        self.setLayer2.setSizePolicy(sizePolicy)
        self.setLayer2.setObjectName(_fromUtf8("setLayer2"))
        self.vboxlayout4.addWidget(self.setLayer2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.vboxlayout4.addItem(spacerItem1)
        self.hboxlayout4.addLayout(self.vboxlayout4)
        self.hboxlayout5 = QtGui.QHBoxLayout()
        self.hboxlayout5.setObjectName(_fromUtf8("hboxlayout5"))
        self.vboxlayout5 = QtGui.QVBoxLayout()
        self.vboxlayout5.setObjectName(_fromUtf8("vboxlayout5"))
        self.label_29 = QtGui.QLabel(self.tab_4)
        self.label_29.setText(QtGui.QApplication.translate("ProfileBase", "R", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.vboxlayout5.addWidget(self.label_29)
        self.label_30 = QtGui.QLabel(self.tab_4)
        self.label_30.setText(QtGui.QApplication.translate("ProfileBase", "G", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.vboxlayout5.addWidget(self.label_30)
        self.label_31 = QtGui.QLabel(self.tab_4)
        self.label_31.setText(QtGui.QApplication.translate("ProfileBase", "B", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.vboxlayout5.addWidget(self.label_31)
        self.hboxlayout5.addLayout(self.vboxlayout5)
        self.vboxlayout6 = QtGui.QVBoxLayout()
        self.vboxlayout6.setObjectName(_fromUtf8("vboxlayout6"))
        self.setR2 = QtGui.QSlider(self.tab_4)
        self.setR2.setMinimumSize(QtCore.QSize(35, 0))
        self.setR2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.setR2.setOrientation(QtCore.Qt.Horizontal)
        self.setR2.setObjectName(_fromUtf8("setR2"))
        self.vboxlayout6.addWidget(self.setR2)
        self.setG2 = QtGui.QSlider(self.tab_4)
        self.setG2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.setG2.setOrientation(QtCore.Qt.Horizontal)
        self.setG2.setObjectName(_fromUtf8("setG2"))
        self.vboxlayout6.addWidget(self.setG2)
        self.setB2 = QtGui.QSlider(self.tab_4)
        self.setB2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.setB2.setOrientation(QtCore.Qt.Horizontal)
        self.setB2.setObjectName(_fromUtf8("setB2"))
        self.vboxlayout6.addWidget(self.setB2)
        self.hboxlayout5.addLayout(self.vboxlayout6)
        self.colorBox2 = QtGui.QGraphicsView(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorBox2.sizePolicy().hasHeightForWidth())
        self.colorBox2.setSizePolicy(sizePolicy)
        self.colorBox2.setMaximumSize(QtCore.QSize(50, 50))
        self.colorBox2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.colorBox2.setAcceptDrops(False)
        self.colorBox2.setObjectName(_fromUtf8("colorBox2"))
        self.hboxlayout5.addWidget(self.colorBox2)
        self.hboxlayout4.addLayout(self.hboxlayout5)
        self.gridlayout6.addLayout(self.hboxlayout4, 1, 0, 1, 1)
        self.hboxlayout6 = QtGui.QHBoxLayout()
        self.hboxlayout6.setObjectName(_fromUtf8("hboxlayout6"))
        self.vboxlayout7 = QtGui.QVBoxLayout()
        self.vboxlayout7.setObjectName(_fromUtf8("vboxlayout7"))
        self.label_32 = QtGui.QLabel(self.tab_4)
        self.label_32.setText(QtGui.QApplication.translate("ProfileBase", "Profile 3:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.vboxlayout7.addWidget(self.label_32)
        self.setLayer3 = QtGui.QComboBox(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setLayer3.sizePolicy().hasHeightForWidth())
        self.setLayer3.setSizePolicy(sizePolicy)
        self.setLayer3.setObjectName(_fromUtf8("setLayer3"))
        self.vboxlayout7.addWidget(self.setLayer3)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.vboxlayout7.addItem(spacerItem2)
        self.hboxlayout6.addLayout(self.vboxlayout7)
        self.hboxlayout7 = QtGui.QHBoxLayout()
        self.hboxlayout7.setObjectName(_fromUtf8("hboxlayout7"))
        self.vboxlayout8 = QtGui.QVBoxLayout()
        self.vboxlayout8.setObjectName(_fromUtf8("vboxlayout8"))
        self.label_33 = QtGui.QLabel(self.tab_4)
        self.label_33.setText(QtGui.QApplication.translate("ProfileBase", "R", None, QtGui.QApplication.UnicodeUTF8))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.vboxlayout8.addWidget(self.label_33)
        self.label_34 = QtGui.QLabel(self.tab_4)
        self.label_34.setText(QtGui.QApplication.translate("ProfileBase", "G", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.vboxlayout8.addWidget(self.label_34)
        self.label_35 = QtGui.QLabel(self.tab_4)
        self.label_35.setText(QtGui.QApplication.translate("ProfileBase", "B", None, QtGui.QApplication.UnicodeUTF8))
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.vboxlayout8.addWidget(self.label_35)
        self.hboxlayout7.addLayout(self.vboxlayout8)
        self.vboxlayout9 = QtGui.QVBoxLayout()
        self.vboxlayout9.setObjectName(_fromUtf8("vboxlayout9"))
        self.setR3 = QtGui.QSlider(self.tab_4)
        self.setR3.setMinimumSize(QtCore.QSize(35, 0))
        self.setR3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.setR3.setOrientation(QtCore.Qt.Horizontal)
        self.setR3.setObjectName(_fromUtf8("setR3"))
        self.vboxlayout9.addWidget(self.setR3)
        self.setG3 = QtGui.QSlider(self.tab_4)
        self.setG3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.setG3.setOrientation(QtCore.Qt.Horizontal)
        self.setG3.setObjectName(_fromUtf8("setG3"))
        self.vboxlayout9.addWidget(self.setG3)
        self.setB3 = QtGui.QSlider(self.tab_4)
        self.setB3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.setB3.setOrientation(QtCore.Qt.Horizontal)
        self.setB3.setObjectName(_fromUtf8("setB3"))
        self.vboxlayout9.addWidget(self.setB3)
        self.hboxlayout7.addLayout(self.vboxlayout9)
        self.colorBox3 = QtGui.QGraphicsView(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorBox3.sizePolicy().hasHeightForWidth())
        self.colorBox3.setSizePolicy(sizePolicy)
        self.colorBox3.setMaximumSize(QtCore.QSize(50, 50))
        self.colorBox3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.colorBox3.setAcceptDrops(False)
        self.colorBox3.setObjectName(_fromUtf8("colorBox3"))
        self.hboxlayout7.addWidget(self.colorBox3)
        self.hboxlayout6.addLayout(self.hboxlayout7)
        self.gridlayout6.addLayout(self.hboxlayout6, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridlayout7 = QtGui.QGridLayout(self.tab_3)
        self.gridlayout7.setObjectName(_fromUtf8("gridlayout7"))
        self.label_3 = QtGui.QLabel(self.tab_3)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_3.setText(QtGui.QApplication.translate("ProfileBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Profile Tool Plugin</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Profile Plugin plots terrain profiles along interactive pointed polylines. It handles  any format supported by QGis. You can compare up to three layers together, control height scale and line colors. Unfortunately it has huge requirements: development version of QGIS and Qwt5.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Please send me your reflections, opinions, suggestions and wishes (especially related to this plugin;) on <a href=\"http://hub.qgis.org/projects/profiletool/issues\"><span style=\" text-decoration: underline; color:#0000ff;\">http://hub.qgis.org/projects/profiletool/issues</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you find this plugin useful please don\'t hesitate to let me know desired improvements!</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Profile Tool Plugin - License GNU GPL 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Written in 2008 by Borys Jurgiel (borys@wolf.most.org.pl)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Written in 2012 by Borys Jurgiel, Patrice Verchere</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">REQUIREMENTS:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Qwt5 (python-qwt5-qt4)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- QT ver 4.1 for saving to PDF and 4.3 for saving to SVG</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridlayout7.addWidget(self.label_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.gridlayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.hboxlayout8 = QtGui.QHBoxLayout()
        self.hboxlayout8.setObjectName(_fromUtf8("hboxlayout8"))
        spacerItem3 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.hboxlayout8.addItem(spacerItem3)
        self.butPrint = QtGui.QPushButton(ProfileBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butPrint.sizePolicy().hasHeightForWidth())
        self.butPrint.setSizePolicy(sizePolicy)
        self.butPrint.setMinimumSize(QtCore.QSize(100, 0))
        self.butPrint.setText(QtGui.QApplication.translate("ProfileBase", "Print", None, QtGui.QApplication.UnicodeUTF8))
        self.butPrint.setObjectName(_fromUtf8("butPrint"))
        self.hboxlayout8.addWidget(self.butPrint)
        self.butPDF = QtGui.QPushButton(ProfileBase)
        self.butPDF.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butPDF.sizePolicy().hasHeightForWidth())
        self.butPDF.setSizePolicy(sizePolicy)
        self.butPDF.setMinimumSize(QtCore.QSize(100, 0))
        self.butPDF.setText(QtGui.QApplication.translate("ProfileBase", "Save as PDF", None, QtGui.QApplication.UnicodeUTF8))
        self.butPDF.setObjectName(_fromUtf8("butPDF"))
        self.hboxlayout8.addWidget(self.butPDF)
        self.butSVG = QtGui.QPushButton(ProfileBase)
        self.butSVG.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butSVG.sizePolicy().hasHeightForWidth())
        self.butSVG.setSizePolicy(sizePolicy)
        self.butSVG.setMinimumSize(QtCore.QSize(100, 0))
        self.butSVG.setText(QtGui.QApplication.translate("ProfileBase", "Save as SVG", None, QtGui.QApplication.UnicodeUTF8))
        self.butSVG.setObjectName(_fromUtf8("butSVG"))
        self.hboxlayout8.addWidget(self.butSVG)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout8.addItem(spacerItem4)
        self.buttonBox = QtGui.QDialogButtonBox(ProfileBase)
        self.buttonBox.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.hboxlayout8.addWidget(self.buttonBox)
        self.gridlayout.addLayout(self.hboxlayout8, 1, 0, 1, 1)

        self.retranslateUi(ProfileBase)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ProfileBase.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ProfileBase.reject)
        QtCore.QMetaObject.connectSlotsByName(ProfileBase)
        ProfileBase.setTabOrder(self.buttonBox, self.tabWidget)
        ProfileBase.setTabOrder(self.tabWidget, self.scaleSlider)
        ProfileBase.setTabOrder(self.scaleSlider, self.butPrint)
        ProfileBase.setTabOrder(self.butPrint, self.butPDF)
        ProfileBase.setTabOrder(self.butPDF, self.butSVG)
        ProfileBase.setTabOrder(self.butSVG, self.setLayer1)
        ProfileBase.setTabOrder(self.setLayer1, self.setLayer2)
        ProfileBase.setTabOrder(self.setLayer2, self.setLayer3)
        ProfileBase.setTabOrder(self.setLayer3, self.setR1)
        ProfileBase.setTabOrder(self.setR1, self.setG1)
        ProfileBase.setTabOrder(self.setG1, self.setB1)
        ProfileBase.setTabOrder(self.setB1, self.setR2)
        ProfileBase.setTabOrder(self.setR2, self.setG2)
        ProfileBase.setTabOrder(self.setG2, self.setB2)
        ProfileBase.setTabOrder(self.setB2, self.setR3)
        ProfileBase.setTabOrder(self.setR3, self.setG3)
        ProfileBase.setTabOrder(self.setG3, self.setB3)

    def retranslateUi(self, ProfileBase):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("ProfileBase", "&Profile", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("ProfileBase", "&Statistics", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("ProfileBase", "S&etup", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("ProfileBase", "&About", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4.Qwt5 import QwtPlot
