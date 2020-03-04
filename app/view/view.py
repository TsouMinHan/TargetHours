from PyQt5.QtWidgets import QApplication, QmainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

from .ui import Ui_MainWindow

class View(QMainWindow, Ui_MainWindow):
    def __init(self, parent=None):
        super(View, self).__init__(parent)
        self.setupUi(self)

        