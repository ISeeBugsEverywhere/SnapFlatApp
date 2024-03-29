# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SnapFlatApp.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SFA_main_window(object):
    def setupUi(self, SFA_main_window):
        SFA_main_window.setObjectName("SFA_main_window")
        SFA_main_window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SFA_main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(32, 32))
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setObjectName("tabWidget")
        self.snapcraftTab = QtWidgets.QWidget()
        self.snapcraftTab.setObjectName("snapcraftTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.snapcraftTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(self.snapcraftTab)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.snapGroupedListView = QtWidgets.QListView(self.splitter)
        self.snapGroupedListView.setMaximumSize(QtCore.QSize(300, 16777215))
        self.snapGroupedListView.setObjectName("snapGroupedListView")
        self.snapsSortedView = QtWidgets.QTableWidget(self.splitter)
        self.snapsSortedView.setObjectName("snapsSortedView")
        self.snapsSortedView.setColumnCount(0)
        self.snapsSortedView.setRowCount(0)
        self.gridLayout_2.addWidget(self.splitter, 1, 0, 1, 5)
        self.getRemoveSnapButton = QtWidgets.QPushButton(self.snapcraftTab)
        self.getRemoveSnapButton.setObjectName("getRemoveSnapButton")
        self.gridLayout_2.addWidget(self.getRemoveSnapButton, 2, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(518, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 2, 1, 3)
        self.iconLabel = QtWidgets.QGraphicsView(self.snapcraftTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iconLabel.sizePolicy().hasHeightForWidth())
        self.iconLabel.setSizePolicy(sizePolicy)
        self.iconLabel.setMaximumSize(QtCore.QSize(64, 64))
        self.iconLabel.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.iconLabel.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.iconLabel.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.iconLabel.setObjectName("iconLabel")
        self.gridLayout_2.addWidget(self.iconLabel, 0, 0, 1, 1)
        self.searchSnapsButton = QtWidgets.QPushButton(self.snapcraftTab)
        self.searchSnapsButton.setMaximumSize(QtCore.QSize(120, 31))
        self.searchSnapsButton.setObjectName("searchSnapsButton")
        self.gridLayout_2.addWidget(self.searchSnapsButton, 0, 4, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.snapcraftTab)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 3)
        self.tabWidget.addTab(self.snapcraftTab, "")
        self.flatpakTab = QtWidgets.QWidget()
        self.flatpakTab.setObjectName("flatpakTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.flatpakTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.flatpakIcon = QtWidgets.QGraphicsView(self.flatpakTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flatpakIcon.sizePolicy().hasHeightForWidth())
        self.flatpakIcon.setSizePolicy(sizePolicy)
        self.flatpakIcon.setMaximumSize(QtCore.QSize(64, 64))
        self.flatpakIcon.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.flatpakIcon.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.flatpakIcon.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.flatpakIcon.setObjectName("flatpakIcon")
        self.gridLayout_3.addWidget(self.flatpakIcon, 0, 0, 1, 1)
        self.flatpak_search_field = QtWidgets.QLineEdit(self.flatpakTab)
        self.flatpak_search_field.setObjectName("flatpak_search_field")
        self.gridLayout_3.addWidget(self.flatpak_search_field, 0, 1, 1, 2)
        self.searchSnapsButton_2 = QtWidgets.QPushButton(self.flatpakTab)
        self.searchSnapsButton_2.setMaximumSize(QtCore.QSize(120, 31))
        self.searchSnapsButton_2.setObjectName("searchSnapsButton_2")
        self.gridLayout_3.addWidget(self.searchSnapsButton_2, 0, 3, 1, 1)
        self.getRemoveFlatPakButton = QtWidgets.QPushButton(self.flatpakTab)
        self.getRemoveFlatPakButton.setObjectName("getRemoveFlatPakButton")
        self.gridLayout_3.addWidget(self.getRemoveFlatPakButton, 2, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(478, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 2, 2, 1, 2)
        self.splitter_2 = QtWidgets.QSplitter(self.flatpakTab)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.flatsGroupedView = QtWidgets.QListView(self.splitter_2)
        self.flatsGroupedView.setMaximumSize(QtCore.QSize(300, 16777215))
        self.flatsGroupedView.setObjectName("flatsGroupedView")
        self.flatsSortedView = QtWidgets.QTableWidget(self.splitter_2)
        self.flatsSortedView.setObjectName("flatsSortedView")
        self.flatsSortedView.setColumnCount(0)
        self.flatsSortedView.setRowCount(0)
        self.gridLayout_3.addWidget(self.splitter_2, 1, 0, 1, 4)
        self.tabWidget.addTab(self.flatpakTab, "")
        self.appimageTab = QtWidgets.QWidget()
        self.appimageTab.setObjectName("appimageTab")
        self.tabWidget.addTab(self.appimageTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        SFA_main_window.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(SFA_main_window)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuPreferencies = QtWidgets.QMenu(self.menuBar)
        self.menuPreferencies.setObjectName("menuPreferencies")
        SFA_main_window.setMenuBar(self.menuBar)
        self.actionQuit = QtWidgets.QAction(SFA_main_window)
        self.actionQuit.setObjectName("actionQuit")
        self.actionPaths = QtWidgets.QAction(SFA_main_window)
        self.actionPaths.setObjectName("actionPaths")
        self.menuFile.addAction(self.actionQuit)
        self.menuPreferencies.addAction(self.actionPaths)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuPreferencies.menuAction())

        self.retranslateUi(SFA_main_window)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(SFA_main_window)

    def retranslateUi(self, SFA_main_window):
        _translate = QtCore.QCoreApplication.translate
        SFA_main_window.setWindowTitle(_translate("SFA_main_window", "SnapFlatApp"))
        self.getRemoveSnapButton.setText(_translate("SFA_main_window", "Add/Remove Selected Snap"))
        self.searchSnapsButton.setText(_translate("SFA_main_window", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.snapcraftTab), _translate("SFA_main_window", "Snapcraft Store"))
        self.searchSnapsButton_2.setText(_translate("SFA_main_window", "Search"))
        self.getRemoveFlatPakButton.setText(_translate("SFA_main_window", "Add/Remove Selected Flats"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.flatpakTab), _translate("SFA_main_window", "Flatpak Hub"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.appimageTab), _translate("SFA_main_window", "AppImage(s)"))
        self.menuFile.setTitle(_translate("SFA_main_window", "Fi&le"))
        self.menuPreferencies.setTitle(_translate("SFA_main_window", "Prefere&nces"))
        self.actionQuit.setText(_translate("SFA_main_window", "&Quit"))
        self.actionPaths.setText(_translate("SFA_main_window", "&Paths..."))

