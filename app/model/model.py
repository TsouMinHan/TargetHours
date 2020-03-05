from . import DBHandler

class Model():
    def __init__(self):
        pass

    def insert_to_db(self, title, target, owe, now):
        print('insert!')
        with DBHandler.DBHandler():
            DBHandler.insert(title, target, owe, now)

    def search_title(self, title):
        """
        Return result number. 1 or 0.
        """
        print('search!')
        with DBHandler.DBHandler():
            num = DBHandler.search(title)
        return num
    
    def get_all_record(self,):
        with DBHandler.DBHandler():
            result = list(DBHandler.yield_all_record())
        return result

    def delete_data(self, title):
        print(f'delete_data {title}')
        with DBHandler.DBHandler():
            DBHandler.delete_data(title)
     
if __name__ == '__main__':
    pass
