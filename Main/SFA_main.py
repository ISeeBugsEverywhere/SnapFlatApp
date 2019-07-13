from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.SnapFlatApp import Ui_SFA_main_window

class SFA_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(SFA_window, self).__init__()
        self.ui = Ui_SFA_main_window()
        self.ui.setupUi(self)
        self.__setup_UI()
        pass

    def __setup_UI(self):
        picture = QtGui.QPixmap('GUI/Icons/snap.png')
        scene = QtWidgets.QGraphicsScene()
        scene.setSceneRect(0,0,64,64)
        scene.addItem(QtWidgets.QGraphicsPixmapItem(picture))
        self.ui.iconLabel.setScene(scene)
        #self.ui.iconLabel.fitInView(scene.sceneRect(), QtCore.Qt.KeepAspectRatio)
        pass