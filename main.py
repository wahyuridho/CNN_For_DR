import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from design_interfaces import Ui_MainWindow
from function import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.ui.minimizeButton.clicked.connect(lambda : self.showMinimized())
        self.ui.closeButton.clicked.connect(lambda : self.close())
        self.ui.btn_toogle.clicked.connect(lambda: UIFunctions.slideLeftMenu(self, 120, True))

        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        self.ui.main_header.mouseMoveEvent = moveWindow

        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
        self.ui.btn_home.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.home))
        self.ui.btn_informasi.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.informasi))
        self.ui.btn_setting.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.setting))

        self.ui.btn_browse.clicked.connect(lambda : UIFunctions.select_file(self, True))

        self.show()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
