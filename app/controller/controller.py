from PyQt5 import QtWidgets
import sys

from app.view import View
from app.model import Model

class Controller:
    def __init__(self):
        self._app = QtWidgets.QApplication(sys.argv)
        self._model = Model()
        self._view = View()

        self.init()

    def init(self,):

        self._view.add_btn.clicked.connect(
            lambda: self.insert_to_db(
                self._view.title_lineEdit.text(),
                self._view.time_lineEdit.text())
            )

    def validate_time(self, time: str):
        try:            
            return int(time)
        except ValueError:
            # TODO show msg box.
            print("Invalid time.")
            return False

    def insert_to_db(self, title: str, time:str):
        validated_time = self.validate_time(time)
        if validated_time:
            self._model.insert_to_db(title, validated_time, 0, 0)

    def run(self):
        self._view.show()
        return self._app.exec_()
        
if __name__ == '__main__':
    pass
    
