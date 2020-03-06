from PyQt5 import QtWidgets
from datetime import datetime
import time
import sys

from app.view import View
from app.model import Model
from .addThread import AddThread
from .timerThread import TimerThread

class Controller:
    def __init__(self):
        self._app = QtWidgets.QApplication(sys.argv)
        self._model = Model()
        self._view = View()

        self.add_thread = AddThread()
        self.timer_thread = TimerThread()
        self.init()

    def init(self,):
        self.set_table_and_combox()

        self.add_thread.add_to_table_signal.connect(lambda: self._view.add_to_table(self.add_thread.items))
        
        self.timer_thread.set_label_signal.connect(self._view.set_label)
        self.timer_thread.update_signal.connect(self.update_data)

        self._view.add_btn.clicked.connect(
            lambda: self.insert_to_db(
                self._view.title_lineEdit.text(),
                self._view.time_lineEdit.text())
            )
        self._view.reset_btn.clicked.connect(self.settlement)
        self._view.delete_btn.clicked.connect(self.delete_data)
        self._view.play_btn.clicked.connect(self.start_playing)
        self._view.pause_btn.clicked.connect(self.pause_playing)
        self._view.stop_btn.clicked.connect(self.stop_playing)

    def settlement(self,):
        items = self._model.get_all_record()
        for item in items:
            title = item[0]
            target = item[1]
            owe = item[2]
            now = item[3]
            record_target = item[4]

            if owe!=0:
                owe -= now
                if owe<0:
                    target += owe
                    owe = 0
                    if target<0:
                        target = 0
            else:
                target -= now
                if target<0:
                    target = 0
                    
            owe += target
            self._model.reset_record(title, owe, 0, record_target)
            self.set_table_and_combox()

    def update_data(self, item: tuple):
        self._model.update_data(item[0], item[1], item[2], item[3])
        self.set_table_and_combox()

    def stop_playing(self,):
        self.timer_thread.stop_flag = True

    def pause_playing(self,):
        self.timer_thread.pause_flag = not self.timer_thread.pause_flag

    def start_playing(self,):
        if self.timer_thread.isRunning():
            self.pause_playing()
        else:
            self.timer_thread.title = self._view.comboBox.currentText()
            item = self._model.get_data('title', self.timer_thread.title)
            _, self.timer_thread.target, self.timer_thread.owe, self.timer_thread.now = item

            self.timer_thread.start()

    def delete_data(self,):
        items = self._view.tableWidget.selectionModel().selectedRows()
        for item in items:
            row = item.row()
            title = self._view.tableWidget.item(row, 0).text()

            self._model.delete_data(title)

            self._view.tableWidget.removeRow(row)

    def validate_title(self, title: str):
        if title.isdigit():            
            return False

        return not self._model.search_title(title)

    def validate_time(self, time: str):
        try:            
            return int(time)
        except ValueError:            
            print("Invalid time.")
            return False

    def insert_to_db(self, title: str, time:str):
        validated_title = self.validate_title(title)*60
        validated_time = self.validate_time(time)*60

        if validated_title and validated_time:
            self._model.insert_to_db(title, validated_time, 0, 0)
            try:
                # set items
                self.add_thread.items = (title, validated_time, 0, 0)
                self.add_thread.start()
            except Exception as e:
                print(e)
        else:
            if title.isdigit():
                self._view.msgBox(f'<{title}> cannot only construct by number.')
            else:
                self._view.msgBox(f'<{title}> has repeat or time invalid failed.')

    def set_table_and_combox(self,):
        self._view.tableWidget.clear()
        self._view.tableWidget.setRowCount(0)

        items = self._model.get_all_record()
        for item in items:
            self._view.add_to_table(item)
            self._view.comboBox.addItem(item[0])

    def run(self):
        self._view.show()
        return self._app.exec_()
        
if __name__ == '__main__':
    pass
    
