import sqlite3

global conn, cur

table_name = 'list_table'
db_name = r'doc\app.db'
class DBHandler():
    def __enter__(self):
        self.start_database()
        return self

    def __exit__(self, exc_type, ex_value, ex_traceback):
        self.close_database()
    
    def start_database(self,):
        global conn, cur
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()

    def close_database(self,):
        """shut down connect to DB
        """
        global conn
        conn.close()

def insert(title, target, owe, now):
    global conn, cur
    sql = f"INSERT INTO {table_name} "\
        f"(title, target, owe, now) VALUES ('{title}','{target}','{owe}', '{now}')"
    cur.execute(sql)
    conn.commit()

if __name__ == '__main__':
    pass
