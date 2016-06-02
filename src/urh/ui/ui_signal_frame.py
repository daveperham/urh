# -*- coding: utf-8 -*-

#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SignalFrame(object):
    def setupUi(self, SignalFrame):
        SignalFrame.setObjectName("SignalFrame")
        SignalFrame.resize(1057, 439)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SignalFrame.sizePolicy().hasHeightForWidth())
        SignalFrame.setSizePolicy(sizePolicy)
        SignalFrame.setMinimumSize(QtCore.QSize(0, 0))
        SignalFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        SignalFrame.setSizeIncrement(QtCore.QSize(0, 0))
        SignalFrame.setBaseSize(QtCore.QSize(0, 0))
        SignalFrame.setMouseTracking(False)
        SignalFrame.setAcceptDrops(True)
        SignalFrame.setAutoFillBackground(False)
        SignalFrame.setStyleSheet("")
        SignalFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        SignalFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.horizontalLayout = QtWidgets.QHBoxLayout(SignalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.chkBoxSyncSelection = QtWidgets.QCheckBox(SignalFrame)
        self.chkBoxSyncSelection.setChecked(True)
        self.chkBoxSyncSelection.setObjectName("chkBoxSyncSelection")
        self.gridLayout_2.addWidget(self.chkBoxSyncSelection, 19, 0, 1, 1)
        self.spinBoxNoiseTreshold = QtWidgets.QDoubleSpinBox(SignalFrame)
        self.spinBoxNoiseTreshold.setDecimals(4)
        self.spinBoxNoiseTreshold.setMaximum(1.0)
        self.spinBoxNoiseTreshold.setSingleStep(0.0001)
        self.spinBoxNoiseTreshold.setObjectName("spinBoxNoiseTreshold")
        self.gridLayout_2.addWidget(self.spinBoxNoiseTreshold, 2, 1, 1, 1)
        self.chkBoxShowProtocol = QtWidgets.QCheckBox(SignalFrame)
        self.chkBoxShowProtocol.setObjectName("chkBoxShowProtocol")
        self.gridLayout_2.addWidget(self.chkBoxShowProtocol, 18, 0, 1, 1)
        self.label = QtWidgets.QLabel(SignalFrame)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.lineEditSignalName = QtWidgets.QLineEdit(SignalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSignalName.sizePolicy().hasHeightForWidth())
        self.lineEditSignalName.setSizePolicy(sizePolicy)
        self.lineEditSignalName.setMinimumSize(QtCore.QSize(214, 0))
        self.lineEditSignalName.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEditSignalName.setFont(font)
        self.lineEditSignalName.setAcceptDrops(False)
        self.lineEditSignalName.setObjectName("lineEditSignalName")
        self.gridLayout_2.addWidget(self.lineEditSignalName, 1, 0, 1, 2)
        self.lInfoLenText = QtWidgets.QLabel(SignalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lInfoLenText.sizePolicy().hasHeightForWidth())
        self.lInfoLenText.setSizePolicy(sizePolicy)
        self.lInfoLenText.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.lInfoLenText.setObjectName("lInfoLenText")
        self.gridLayout_2.addWidget(self.lInfoLenText, 4, 0, 1, 1)
        self.spinBoxInfoLen = QtWidgets.QSpinBox(SignalFrame)
        self.spinBoxInfoLen.setMinimumSize(QtCore.QSize(100, 0))
        self.spinBoxInfoLen.setMinimum(1)
        self.spinBoxInfoLen.setMaximum(999999999)
        self.spinBoxInfoLen.setObjectName("spinBoxInfoLen")
        self.gridLayout_2.addWidget(self.spinBoxInfoLen, 4, 1, 1, 1)
        self.spinBoxTolerance = QtWidgets.QSpinBox(SignalFrame)
        self.spinBoxTolerance.setMinimumSize(QtCore.QSize(100, 0))
        self.spinBoxTolerance.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.spinBoxTolerance.setMaximum(9999)
        self.spinBoxTolerance.setObjectName("spinBoxTolerance")
        self.gridLayout_2.addWidget(self.spinBoxTolerance, 7, 1, 1, 1)
        self.lErrorTolerance = QtWidgets.QLabel(SignalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lErrorTolerance.sizePolicy().hasHeightForWidth())
        self.lErrorTolerance.setSizePolicy(sizePolicy)
        self.lErrorTolerance.setMinimumSize(QtCore.QSize(0, 0))
        self.lErrorTolerance.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lErrorTolerance.setObjectName("lErrorTolerance")
        self.gridLayout_2.addWidget(self.lErrorTolerance, 7, 0, 1, 1)
        self.lSignalViewText = QtWidgets.QLabel(SignalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lSignalViewText.sizePolicy().hasHeightForWidth())
        self.lSignalViewText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.lSignalViewText.setFont(font)
        self.lSignalViewText.setObjectName("lSignalViewText")
        self.gridLayout_2.addWidget(self.lSignalViewText, 13, 0, 1, 1)
        self.cbProtoView = QtWidgets.QComboBox(SignalFrame)
        self.cbProtoView.setObjectName("cbProtoView")
        self.cbProtoView.addItem("")
        self.cbProtoView.addItem("")
        self.cbProtoView.addItem("")
        self.gridLayout_2.addWidget(self.cbProtoView, 18, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btnMinimize = QtWidgets.QToolButton(SignalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMinimize.sizePolicy().hasHeightForWidth())
        self.btnMinimize.setSizePolicy(sizePolicy)
        self.btnMinimize.setMinimumSize(QtCore.QSize(24, 24))
        self.btnMinimize.setMaximumSize(QtCore.QSize(24, 24))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/data/icons/uparrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMinimize.setIcon(icon)
        self.btnMinimize.setIconSize(QtCore.QSize(16, 16))
        self.btnMinimize.setObjectName("btnMinimize")
        self.gridLayout.addWidget(self.btnMinimize, 0, 9, 1, 1)
        self.btnSaveSignal = QtWidgets.QToolButton(SignalFrame)
        self.btnSaveSignal.setMinimumSize(QtCore.QSize(24, 24))
        self.btnSaveSignal.setMaximumSize(QtCore.QSize(24, 24))
        icon = QtGui.QIcon.fromTheme("document-save")
        self.btnSaveSignal.setIcon(icon)
        self.btnSaveSignal.setObjectName("btnSaveSignal")
        self.gridLayout.addWidget(self.btnSaveSignal, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.btnCloseSignal = QtWidgets.QToolButton(SignalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCloseSignal.sizePolicy().hasHeightForWidth())
        self.btnCloseSignal.setSizePolicy(sizePolicy)
        self.btnCloseSignal.setMinimumSize(QtCore.QSize(24, 24))
        self.btnCloseSignal.setMaximumSize(QtCore.QSize(24, 24))
        self.btnCloseSignal.setStyleSheet("color:red;")
        icon = QtGui.QIcon.fromTheme("window-close")
        self.btnCloseSignal.setIcon(icon)
        self.btnCloseSignal.setObjectName("btnCloseSignal")
        self.gridLayout.addWidget(self.btnCloseSignal, 0, 10, 1, 1)
        self.lSignalTyp = QtWidgets.QLabel(SignalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lSignalTyp.sizePolicy().hasHeightForWidth())
        self.lSignalTyp.setSizePolicy(sizePolicy)
        self.lSignalTyp.setObjectName("lSignalTyp")
        self.gridLayout.addWidget(self.lSignalTyp, 0, 1, 1, 1)
        self.lSignalNr = QtWidgets.QLabel(SignalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lSignalNr.sizePolicy().hasHeightForWidth())
        self.lSignalNr.setSizePolicy(sizePolicy)
        self.lSignalNr.setWordWrap(False)
        self.lSignalNr.setIndent(-1)
        self.lSignalNr.setObjectName("lSignalNr")
        self.gridLayout.addWidget(self.lSignalNr, 0, 0, 1, 1)
        self.btnInfo = QtWidgets.QToolButton(SignalFrame)
        self.btnInfo.setMinimumSize(QtCore.QSize(24, 24))
        self.btnInfo.setMaximumSize(QtCore.QSize(24, 24))
        icon = QtGui.QIcon.fromTheme("dialog-information")
        self.btnInfo.setIcon(icon)
        self.btnInfo.setObjectName("btnInfo")
        self.gridLayout.addWidget(self.btnInfo, 0, 6, 1, 1)
        self.btnReplay = QtWidgets.QToolButton(SignalFrame)
        self.btnReplay.setMinimumSize(QtCore.QSize(24, 24))
        self.btnReplay.setMaximumSize(QtCore.QSize(24, 24))
        self.btnReplay.setText("")
        icon = QtGui.QIcon.fromTheme("media-playback-start")
        self.btnReplay.setIcon(icon)
        self.btnReplay.setObjectName("btnReplay")
        self.gridLayout.addWidget(self.btnReplay, 0, 5, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.lCenterOffset = QtWidgets.QLabel(SignalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lCenterOffset.sizePolicy().hasHeightForWidth())
        self.lCenterOffset.setSizePolicy(sizePolicy)
        self.lCenterOffset.setMinimumSize(QtCore.QSize(0, 0))
        self.lCenterOffset.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lCenterOffset.setWhatsThis("")
        self.lCenterOffset.setObjectName("lCenterOffset")
        self.gridLayout_2.addWidget(self.lCenterOffset, 3, 0, 1, 1)
        self.spinBoxCenterOffset = QtWidgets.QDoubleSpinBox(SignalFrame)
        self.spinBoxCenterOffset.setMinimumSize(QtCore.QSize(100, 0))
        self.spinBoxCenterOffset.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.spinBoxCenterOffset.setDecimals(4)
        self.spinBoxCenterOffset.setMinimum(-3.15)
        self.spinBoxCenterOffset.setMaximum(6.28)
        self.spinBoxCenterOffset.setSingleStep(0.0001)
        self.spinBoxCenterOffset.setObjectName("spinBoxCenterOffset")
        self.gridLayout_2.addWidget(self.spinBoxCenterOffset, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(SignalFrame)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 9, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 17, 0, 1, 1)
        self.line = QtWidgets.QFrame(SignalFrame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 11, 0, 1, 2)
        self.line_2 = QtWidgets.QFrame(SignalFrame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 16, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 10, 0, 1, 1)
        self.btnAutoDetect = QtWidgets.QPushButton(SignalFrame)
        icon = QtGui.QIcon.fromTheme("system-software-update")
        self.btnAutoDetect.setIcon(icon)
        self.btnAutoDetect.setIconSize(QtCore.QSize(16, 16))
        self.btnAutoDetect.setCheckable(True)
        self.btnAutoDetect.setChecked(True)
        self.btnAutoDetect.setObjectName("btnAutoDetect")
        self.gridLayout_2.addWidget(self.btnAutoDetect, 15, 0, 1, 2)
        self.cbModulationType = QtWidgets.QComboBox(SignalFrame)
        self.cbModulationType.setObjectName("cbModulationType")
        self.cbModulationType.addItem("")
        self.cbModulationType.addItem("")
        self.cbModulationType.addItem("")
        self.gridLayout_2.addWidget(self.cbModulationType, 9, 1, 1, 1)
        self.cbSignalView = QtWidgets.QComboBox(SignalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbSignalView.sizePolicy().hasHeightForWidth())
        self.cbSignalView.setSizePolicy(sizePolicy)
        self.cbSignalView.setObjectName("cbSignalView")
        self.cbSignalView.addItem("")
        self.cbSignalView.addItem("")
        self.gridLayout_2.addWidget(self.cbSignalView, 13, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.splitter = QtWidgets.QSplitter(SignalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter.setLineWidth(1)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(5)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gvLegend = LegendGraphicView(self.layoutWidget)
        self.gvLegend.setMinimumSize(QtCore.QSize(0, 150))
        self.gvLegend.setMaximumSize(QtCore.QSize(30, 16777215))
        self.gvLegend.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.gvLegend.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gvLegend.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.gvLegend.setInteractive(False)
        self.gvLegend.setResizeAnchor(QtWidgets.QGraphicsView.AnchorViewCenter)
        self.gvLegend.setRubberBandSelectionMode(QtCore.Qt.ContainsItemShape)
        self.gvLegend.setOptimizationFlags(QtWidgets.QGraphicsView.DontSavePainterState)
        self.gvLegend.setObjectName("gvLegend")
        self.horizontalLayout_2.addWidget(self.gvLegend)
        self.gvSignal = EpicGraphicView(self.layoutWidget)
        self.gvSignal.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gvSignal.sizePolicy().hasHeightForWidth())
        self.gvSignal.setSizePolicy(sizePolicy)
        self.gvSignal.setMinimumSize(QtCore.QSize(0, 150))
        self.gvSignal.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gvSignal.setMouseTracking(True)
        self.gvSignal.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.gvSignal.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.gvSignal.setAutoFillBackground(False)
        self.gvSignal.setStyleSheet("")
        self.gvSignal.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.gvSignal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gvSignal.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gvSignal.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.gvSignal.setInteractive(False)
        self.gvSignal.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.TextAntialiasing)
        self.gvSignal.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        self.gvSignal.setCacheMode(QtWidgets.QGraphicsView.CacheNone)
        self.gvSignal.setTransformationAnchor(QtWidgets.QGraphicsView.NoAnchor)
        self.gvSignal.setResizeAnchor(QtWidgets.QGraphicsView.NoAnchor)
        self.gvSignal.setViewportUpdateMode(QtWidgets.QGraphicsView.MinimalViewportUpdate)
        self.gvSignal.setRubberBandSelectionMode(QtCore.Qt.ContainsItemShape)
        self.gvSignal.setOptimizationFlags(QtWidgets.QGraphicsView.DontClipPainter|QtWidgets.QGraphicsView.DontSavePainterState)
        self.gvSignal.setObjectName("gvSignal")
        self.horizontalLayout_2.addWidget(self.gvSignal)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lYScale = QtWidgets.QLabel(self.layoutWidget)
        self.lYScale.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lYScale.setObjectName("lYScale")
        self.verticalLayout_2.addWidget(self.lYScale)
        self.sliderYScale = QtWidgets.QSlider(self.layoutWidget)
        self.sliderYScale.setMinimum(1)
        self.sliderYScale.setMaximum(100)
        self.sliderYScale.setOrientation(QtCore.Qt.Vertical)
        self.sliderYScale.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sliderYScale.setObjectName("sliderYScale")
        self.verticalLayout_2.addWidget(self.sliderYScale)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnShowHideStartEnd = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnShowHideStartEnd.sizePolicy().hasHeightForWidth())
        self.btnShowHideStartEnd.setSizePolicy(sizePolicy)
        self.btnShowHideStartEnd.setMinimumSize(QtCore.QSize(15, 0))
        self.btnShowHideStartEnd.setMaximumSize(QtCore.QSize(15, 32))
        self.btnShowHideStartEnd.setAutoFillBackground(False)
        self.btnShowHideStartEnd.setStyleSheet("")
        self.btnShowHideStartEnd.setAutoDefault(False)
        self.btnShowHideStartEnd.setDefault(False)
        self.btnShowHideStartEnd.setFlat(False)
        self.btnShowHideStartEnd.setObjectName("btnShowHideStartEnd")
        self.horizontalLayout_3.addWidget(self.btnShowHideStartEnd)
        self.lNumSelectedSamples = QtWidgets.QLabel(self.layoutWidget)
        self.lNumSelectedSamples.setObjectName("lNumSelectedSamples")
        self.horizontalLayout_3.addWidget(self.lNumSelectedSamples)
        self.lTextSelectedSamples = QtWidgets.QLabel(self.layoutWidget)
        self.lTextSelectedSamples.setObjectName("lTextSelectedSamples")
        self.horizontalLayout_3.addWidget(self.lTextSelectedSamples)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lDuration = QtWidgets.QLabel(self.layoutWidget)
        self.lDuration.setObjectName("lDuration")
        self.horizontalLayout_3.addWidget(self.lDuration)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.lZoomText = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lZoomText.sizePolicy().hasHeightForWidth())
        self.lZoomText.setSizePolicy(sizePolicy)
        self.lZoomText.setMinimumSize(QtCore.QSize(0, 0))
        self.lZoomText.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(False)
        self.lZoomText.setFont(font)
        self.lZoomText.setTextFormat(QtCore.Qt.PlainText)
        self.lZoomText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lZoomText.setObjectName("lZoomText")
        self.horizontalLayout_3.addWidget(self.lZoomText)
        self.spinBoxXZoom = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBoxXZoom.setMinimum(100)
        self.spinBoxXZoom.setMaximum(999999999)
        self.spinBoxXZoom.setObjectName("spinBoxXZoom")
        self.horizontalLayout_3.addWidget(self.spinBoxXZoom)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.additionalInfos = QtWidgets.QHBoxLayout()
        self.additionalInfos.setSpacing(6)
        self.additionalInfos.setObjectName("additionalInfos")
        self.lStart = QtWidgets.QLabel(self.layoutWidget)
        self.lStart.setObjectName("lStart")
        self.additionalInfos.addWidget(self.lStart)
        self.spinBoxSelectionStart = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBoxSelectionStart.setReadOnly(False)
        self.spinBoxSelectionStart.setObjectName("spinBoxSelectionStart")
        self.additionalInfos.addWidget(self.spinBoxSelectionStart)
        self.lEnd = QtWidgets.QLabel(self.layoutWidget)
        self.lEnd.setObjectName("lEnd")
        self.additionalInfos.addWidget(self.lEnd)
        self.spinBoxSelectionEnd = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBoxSelectionEnd.setObjectName("spinBoxSelectionEnd")
        self.additionalInfos.addWidget(self.spinBoxSelectionEnd)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.additionalInfos.addItem(spacerItem4)
        self.lSamplesInView = QtWidgets.QLabel(self.layoutWidget)
        self.lSamplesInView.setObjectName("lSamplesInView")
        self.additionalInfos.addWidget(self.lSamplesInView)
        self.lStrich = QtWidgets.QLabel(self.layoutWidget)
        self.lStrich.setObjectName("lStrich")
        self.additionalInfos.addWidget(self.lStrich)
        self.lSamplesTotal = QtWidgets.QLabel(self.layoutWidget)
        self.lSamplesTotal.setObjectName("lSamplesTotal")
        self.additionalInfos.addWidget(self.lSamplesTotal)
        self.lSamplesViewText = QtWidgets.QLabel(self.layoutWidget)
        self.lSamplesViewText.setObjectName("lSamplesViewText")
        self.additionalInfos.addWidget(self.lSamplesViewText)
        self.verticalLayout.addLayout(self.additionalInfos)
        self.txtEdProto = TextEditProtocolView(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtEdProto.sizePolicy().hasHeightForWidth())
        self.txtEdProto.setSizePolicy(sizePolicy)
        self.txtEdProto.setMinimumSize(QtCore.QSize(0, 80))
        self.txtEdProto.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.txtEdProto.setBaseSize(QtCore.QSize(0, 0))
        self.txtEdProto.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.txtEdProto.setAcceptDrops(False)
        self.txtEdProto.setObjectName("txtEdProto")
        self.horizontalLayout.addWidget(self.splitter)

        self.retranslateUi(SignalFrame)
        QtCore.QMetaObject.connectSlotsByName(SignalFrame)
        SignalFrame.setTabOrder(self.btnSaveSignal, self.btnInfo)
        SignalFrame.setTabOrder(self.btnInfo, self.btnMinimize)
        SignalFrame.setTabOrder(self.btnMinimize, self.btnCloseSignal)
        SignalFrame.setTabOrder(self.btnCloseSignal, self.lineEditSignalName)
        SignalFrame.setTabOrder(self.lineEditSignalName, self.spinBoxNoiseTreshold)
        SignalFrame.setTabOrder(self.spinBoxNoiseTreshold, self.spinBoxCenterOffset)
        SignalFrame.setTabOrder(self.spinBoxCenterOffset, self.spinBoxInfoLen)
        SignalFrame.setTabOrder(self.spinBoxInfoLen, self.spinBoxTolerance)
        SignalFrame.setTabOrder(self.spinBoxTolerance, self.chkBoxShowProtocol)
        SignalFrame.setTabOrder(self.chkBoxShowProtocol, self.cbProtoView)
        SignalFrame.setTabOrder(self.cbProtoView, self.chkBoxSyncSelection)
        SignalFrame.setTabOrder(self.chkBoxSyncSelection, self.txtEdProto)
        SignalFrame.setTabOrder(self.txtEdProto, self.gvLegend)
        SignalFrame.setTabOrder(self.gvLegend, self.gvSignal)
        SignalFrame.setTabOrder(self.gvSignal, self.sliderYScale)
        SignalFrame.setTabOrder(self.sliderYScale, self.btnShowHideStartEnd)
        SignalFrame.setTabOrder(self.btnShowHideStartEnd, self.spinBoxSelectionStart)
        SignalFrame.setTabOrder(self.spinBoxSelectionStart, self.spinBoxSelectionEnd)
        SignalFrame.setTabOrder(self.spinBoxSelectionEnd, self.spinBoxXZoom)

    def retranslateUi(self, SignalFrame):
        _translate = QtCore.QCoreApplication.translate
        SignalFrame.setWindowTitle(_translate("SignalFrame", "Frame"))
        self.chkBoxSyncSelection.setToolTip(_translate("SignalFrame", "If this is set to true, your selected protocol bits will show up in the signal view, and vice versa."))
        self.chkBoxSyncSelection.setText(_translate("SignalFrame", "Sync Selection"))
        self.spinBoxNoiseTreshold.setToolTip(_translate("SignalFrame", "<html><head/><body><p>Set the <span style=\" font-weight:600;\">noise magnitude</span> of your signal. You can tune this value to mute noise in your signal and reveal the true data.</p></body></html>"))
        self.chkBoxShowProtocol.setToolTip(_translate("SignalFrame", "Show the extracted protocol based on the parameters InfoLen, PauseLen and ZeroTreshold (in QuadratureDemod-View).\n"
"\n"
"If you want your protocol to be better seperated, edit the PauseLen using right-click menu from a selection in SignalView or ProtocolView."))
        self.chkBoxShowProtocol.setText(_translate("SignalFrame", "Show Signal as"))
        self.label.setToolTip(_translate("SignalFrame", "<html><head/><body><p>Set the <span style=\" font-weight:600;\">noise magnitude</span> of your signal. You can tune this value to mute noise in your signal and reveal the true data.</p></body></html>"))
        self.label.setText(_translate("SignalFrame", "Noise:"))
        self.lineEditSignalName.setText(_translate("SignalFrame", "SignalName"))
        self.lInfoLenText.setToolTip(_translate("SignalFrame", "<html><head/><body><p>This is the length of one (raw) bit <span style=\" font-weight:600;\">in samples</span>.</p><p><br/></p><p>Tune this value using either <span style=\" font-style:italic;\">the spinbox on the right</span> or the <span style=\" font-style:italic;\">context-menu of the SignalView</span>.</p></body></html>"))
        self.lInfoLenText.setText(_translate("SignalFrame", "Bit Length:"))
        self.spinBoxInfoLen.setToolTip(_translate("SignalFrame", "<html><head/><body><p>This is the length of one (raw) bit <span style=\" font-weight:600;\">in samples</span>.</p><p><br/></p><p>Tune this value using either <span style=\" font-style:italic;\">the spinbox on the right</span> or the <span style=\" font-style:italic;\">context-menu of the SignalView</span>.</p></body></html>"))
        self.spinBoxTolerance.setToolTip(_translate("SignalFrame", "<html><head/><body><p>This is the error tolerance for determining the <span style=\" font-weight:600;\">pulse lengths</span> in the demodulated signal.</p><p><span style=\" text-decoration: underline;\">Example:</span> Say, we are reading a ones pulse and the tolerance value was set to 5. Then 5 errors (which must follow sequentially) are accepted.</p><p>Tune this value if you have <span style=\" font-weight:600;\">spiky data</span> after demodulation.</p></body></html>"))
        self.lErrorTolerance.setToolTip(_translate("SignalFrame", "<html><head/><body><p>This is the error tolerance for determining the <span style=\" font-weight:600;\">pulse lengths</span> in the demodulated signal.</p><p><span style=\" text-decoration: underline;\">Example:</span> Say, we are reading a ones pulse and the tolerance value was set to 5. Then 5 errors (which must follow sequentially) are accepted.</p><p>Tune this value if you have <span style=\" font-weight:600;\">spiky data</span> after demodulation.</p></body></html>"))
        self.lErrorTolerance.setText(_translate("SignalFrame", "Error Tolerance:"))
        self.lSignalViewText.setText(_translate("SignalFrame", "Signal View:"))
        self.cbProtoView.setItemText(0, _translate("SignalFrame", "Bits"))
        self.cbProtoView.setItemText(1, _translate("SignalFrame", "Hex"))
        self.cbProtoView.setItemText(2, _translate("SignalFrame", "ASCII"))
        self.btnMinimize.setText(_translate("SignalFrame", "..."))
        self.btnSaveSignal.setText(_translate("SignalFrame", "..."))
        self.btnCloseSignal.setText(_translate("SignalFrame", "X"))
        self.lSignalTyp.setText(_translate("SignalFrame", "<Signaltyp>"))
        self.lSignalNr.setText(_translate("SignalFrame", "1:"))
        self.btnInfo.setText(_translate("SignalFrame", "..."))
        self.btnReplay.setToolTip(_translate("SignalFrame", "Replay signal"))
        self.lCenterOffset.setToolTip(_translate("SignalFrame", "<html><head/><body><p>This is the threshold used for determining if a <span style=\" font-weight:600;\">bit is one or zero</span>. You can set it here or grab the middle of the area in <span style=\" font-style:italic;\">Quadrature Demod View.</span></p></body></html>"))
        self.lCenterOffset.setText(_translate("SignalFrame", "Center:"))
        self.spinBoxCenterOffset.setToolTip(_translate("SignalFrame", "<html><head/><body><p>This is the threshold used for determining if a <span style=\" font-weight:600;\">bit is one or zero</span>. You can set it here or grab the middle of the area in <span style=\" font-style:italic;\">Quadrature Demod View</span>.</p></body></html>"))
        self.label_2.setText(_translate("SignalFrame", "Modulation:"))
        self.btnAutoDetect.setToolTip(_translate("SignalFrame", "<html><head/><body><p>Automatically detect Center and Bit Length, when you change the demodulation type. You can disable this behaviour for faster switching between demodulations.</p></body></html>"))
        self.btnAutoDetect.setText(_translate("SignalFrame", "Autodetect parameters"))
        self.cbModulationType.setToolTip(_translate("SignalFrame", "<html><head/><body><p>Choose signals modulation:</p><ul><li>Amplitude Shift Keying (ASK)</li><li>Frequency Shift Keying (FSK)</li><li>Phase Shift Keying (PSK)</li></ul></body></html>"))
        self.cbModulationType.setItemText(0, _translate("SignalFrame", "ASK"))
        self.cbModulationType.setItemText(1, _translate("SignalFrame", "FSK"))
        self.cbModulationType.setItemText(2, _translate("SignalFrame", "PSK"))
        self.cbSignalView.setToolTip(_translate("SignalFrame", "<html><head/><body><p>Choose the view of your signal.</p><p>The quadrature demodulation uses a <span style=\" text-decoration: underline;\">treshold of magnitude,</span> to <span style=\" font-weight:600;\">supress noise</span>. All samples with a magnitude lower than this treshold will be eliminated (set to <span style=\" font-style:italic;\">-127</span>) after demod.</p><p>Tune this value by selecting a <span style=\" font-style:italic;\">noisy area</span> and mark it as noise using <span style=\" text-decoration: underline;\">context menu</span>.</p><p>Current noise treshold is: </p></body></html>"))
        self.cbSignalView.setItemText(0, _translate("SignalFrame", "analog"))
        self.cbSignalView.setItemText(1, _translate("SignalFrame", "demodulated"))
        self.lYScale.setText(_translate("SignalFrame", "Y-Scale"))
        self.btnShowHideStartEnd.setText(_translate("SignalFrame", "-"))
        self.lNumSelectedSamples.setToolTip(_translate("SignalFrame", "Number of currently selected samples."))
        self.lNumSelectedSamples.setText(_translate("SignalFrame", "0"))
        self.lTextSelectedSamples.setToolTip(_translate("SignalFrame", "Number of currently selected samples."))
        self.lTextSelectedSamples.setText(_translate("SignalFrame", "samples selected"))
        self.label_3.setText(_translate("SignalFrame", "|"))
        self.lDuration.setText(_translate("SignalFrame", "42 µs"))
        self.lZoomText.setToolTip(_translate("SignalFrame", "<html><head/><body><p>Current (relative) Zoom. Standard is 100%, if you zoom in, this factor increases. You can directly set a value in the spinbox or use the <span style=\" font-weight:600;\">mousewheel to zoom</span>.</p></body></html>"))
        self.lZoomText.setText(_translate("SignalFrame", "X-Zoom:"))
        self.spinBoxXZoom.setToolTip(_translate("SignalFrame", "<html><head/><body><p>Current (relative) Zoom. Standard is 100%, if you zoom in, this factor increases. You can directly set a value in the spinbox or use the <span style=\" font-weight:600;\">mousewheel to zoom</span>.</p></body></html>"))
        self.spinBoxXZoom.setSuffix(_translate("SignalFrame", "%"))
        self.lStart.setText(_translate("SignalFrame", "Start:"))
        self.lEnd.setText(_translate("SignalFrame", "End:"))
        self.lSamplesInView.setText(_translate("SignalFrame", "0"))
        self.lStrich.setText(_translate("SignalFrame", "/"))
        self.lSamplesTotal.setText(_translate("SignalFrame", "0"))
        self.lSamplesViewText.setText(_translate("SignalFrame", "Samples in View"))

from urh.ui.views.EpicGraphicView import EpicGraphicView
from urh.ui.views.LegendGraphicView import LegendGraphicView
from urh.ui.views.TextEditProtocolView import TextEditProtocolView
from . import urh_rc
