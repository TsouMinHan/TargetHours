from . import DBHandler

class Model():
    def __init__(self):
        pass

    def insert_to_db(self, title, target, owe, now):
        print('insert!')
        with DBHandler.DBHandler():
            DBHandler.insert(title, target, owe, now)

if __name__ == '__main__':
    pass
