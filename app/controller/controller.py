from PyQt5 import QtWidgets
import sys

from app.view import View
from app.model import Model
from .addThread import AddThread

class Controller:
    def __init__(self):
        self._app = QtWidgets.QApplication(sys.argv)
        self._model = Model()
        self._view = View()

        self.add_thread = AddThread()
        self.init()

    def init(self,):
        self.set_table_and_combox()

        self.add_thread.add_to_table_signal.connect(lambda: self._view.add_to_table(self.add_thread.items))
        
        self._view.add_btn.clicked.connect(
            lambda: self.insert_to_db(
                self._view.title_lineEdit.text(),
                self._view.time_lineEdit.text())
            )
        self._view.delete_btn.clicked.connect(self.delete_data)
        self._view.play_btn.clicked.connect(self.start_playing)

    def start_playing(sefl,):
        pass
    def delete_data(self,):
        items = self._view.tableWidget.selectionModel().selectedRows()
        for item in items:
            row = item.row()
            title = self._view.tableWidget.item(row, 0).text()

            self._model.delete_data(title)

            self._view.tableWidget.removeRow(row)

    def validate_title(self, title: str):
        if title.isdigit():
            # TODO show msg box
            print(f'{title} cannot only construct by number.')
            return False

        return not self._model.search_title(title)

    def validate_time(self, time: str):
        try:            
            return int(time)
        except ValueError:            
            print("Invalid time.")
            return False

    def insert_to_db(self, title: str, time:str):
        validated_title = self.validate_title(title)
        validated_time = self.validate_time(time)

        if validated_title and validated_time:
            self._model.insert_to_db(title, validated_time, 0, 0)
            try:
                # self._view.add_to_table(title, validated_time, 0, 0)
                # set items
                self.add_thread.items = (title, validated_time, 0, 0)
                self.add_thread.start()
            except Exception as e:
                print(e)
        else:
            # TODO show msg box.
            print(f'{title} has repeat or time invalid failed.')

    def set_table_and_combox(self,):
        items = self._model.get_all_record()
        for item in items:
            self._view.add_to_table(item)
            print(item[0])
            self._view.comboBox.addItem(item[0])

    def run(self):
        self._view.show()
        return self._app.exec_()
        
if __name__ == '__main__':
    pass
    
