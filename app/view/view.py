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

    def add_to_table(self, items):
        print('Add_to_table!')
        title, target, owe, now = items
        row = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(row+1)
        print(row, title, f'{target}({owe})', now)
        print(self.tableWidget.rowCount())
        self.tableWidget.setItem(row, 0, QTableWidgetItem(title))
        self.tableWidget.setItem(row, 1, QTableWidgetItem(f'{target}({owe})'))
        self.tableWidget.setItem(row, 2, QTableWidgetItem(str(now)))