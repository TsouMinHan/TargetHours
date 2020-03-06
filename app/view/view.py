from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
import time

from .ui import Ui_MainWindow

class View(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(View, self).__init__(parent)
        self.setupUi(self)
        self.init()

    def init(self,):
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.play_btn.setIcon(QIcon(r'doc\play.png'))
        self.stop_btn.setIcon(QIcon(r'doc\stop.png'))
        self.pause_btn.setIcon(QIcon(r'doc\pause.png'))

    def set_label(self, txt):
        self.time_label.setText(txt)

    def add_to_table(self, items):
        title, target, owe, now, _ = items
        row = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(row+1)
        self.tableWidget.setItem(row, 0, QTableWidgetItem(title))
        self.tableWidget.setItem(row, 1, QTableWidgetItem(f'{target}({owe})'))
        self.tableWidget.setItem(row, 2, QTableWidgetItem(str(now)))

    def msgBox(self, msg):
        msgBox = QMessageBox()
        msgBox.setText(msg)
        msgBox.exec_()