from PyQt5 import QtWidgets
import sys

from app.view import View

class Controller:
    def __init__(self):
        self._app = QtWidgets.QApplication(sys.argv)
        # self._model = Model()
        self._view = View()

if __name__ == '__main__':
    pass
    
