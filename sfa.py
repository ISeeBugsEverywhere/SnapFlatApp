#/usr/bin/python3
#-*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication
from Main.SFA_main import SFA_window
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SFA_window()
    window.show()
    sys.exit(app.exec_())

