from PyQt5.QtCore import QThread, pyqtSignal

class AddThread(QThread):
    add_to_table_signal = pyqtSignal(tuple)

    def __init__(self,):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self,):  
        self.add_to_table_signal.emit(self.items)