from PyQt5.QtCore import QThread, pyqtSignal
import datetime
import time

class TimerThread(QThread):
    set_label_signal = pyqtSignal(str)
    update_signal = pyqtSignal(tuple)

    def __init__(self,):
        QThread.__init__(self)
        self.play_flag = True
        self.pause_flag = False
        self.stop_flag = False 

        self.title = None
        self.target = None
        self.owe = None
        self.now = None

    def __del__(self):
        self.wait()

    def save(self,):
        if self.owe!=0:
            self.owe -= self.total_time
            if self.owe<0:
                self.target += self.owe
                self.owe = 0

                if self.target<0:
                    self.target = 0
        else:
            self.target -= self.total_time
            if self.target<0:
                    self.target = 0

        self.now += self.total_time
        self.update_signal.emit((self.title, self.target, self.owe, self.now))

    def run(self,):  
        self.pause_flag = False
        self.stop_flag = False 
        self.total_time = 0

        while self.play_flag:
            if not self.pause_flag:
                time.sleep(1)
                self.total_time += 1
                txt = str(datetime.timedelta(seconds=self.total_time))
                self.set_label_signal.emit(txt)
            else:
                time.sleep(0.3)

            if self.stop_flag:
                self.total_time -= 1 # minus delay
                self.save()
                self.set_label_signal.emit('00:00:00')
                break