# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 700)
        MainWindow.setMaximumSize(QtCore.QSize(400, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 380, 300))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tableView.setFont(font)
        self.tableView.setObjectName("tableView")
        self.title_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.title_lineEdit.setGeometry(QtCore.QRect(10, 330, 100, 30))
        self.title_lineEdit.setObjectName("title_lineEdit")
        self.time_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.time_lineEdit.setGeometry(QtCore.QRect(150, 330, 100, 30))
        self.time_lineEdit.setObjectName("time_lineEdit")
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(290, 330, 100, 30))
        self.add_btn.setObjectName("add_btn")
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(130, 410, 130, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.time_label.setFont(font)
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("time_label")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(70, 540, 60, 60))
        self.start_btn.setText("")
        self.start_btn.setObjectName("start_btn")
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setGeometry(QtCore.QRect(260, 540, 60, 60))
        self.stop_btn.setText("")
        self.stop_btn.setObjectName("stop_btn")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(150, 480, 100, 30))
        self.comboBox.setObjectName("comboBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 25))
        self.menubar.setObjectName("menubar")
        self.menusetting = QtWidgets.QMenu(self.menubar)
        self.menusetting.setObjectName("menusetting")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiontest = QtWidgets.QAction(MainWindow)
        self.actiontest.setObjectName("actiontest")
        self.menusetting.addAction(self.actiontest)
        self.menubar.addAction(self.menusetting.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_btn.setText(_translate("MainWindow", "新增"))
        self.time_label.setText(_translate("MainWindow", "00:00:00"))
        self.menusetting.setTitle(_translate("MainWindow", "setting"))
        self.actiontest.setText(_translate("MainWindow", "test"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

