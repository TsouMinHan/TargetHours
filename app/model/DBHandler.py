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
        f"(title, target, owe, now, record_target) VALUES ('{title}','{target}','{owe}', '{now}', '{target}')"
    cur.execute(sql)
    conn.commit()

def search(title,):
    global conn, cur
    sql = f"SELECT title FROM {table_name} WHERE title='{title}'"
    cur.execute(sql)
    rows = cur.fetchall()
    return len(rows)

def yield_all_record():
    global conn, cur
    sql = f"SELECT title, target, owe, now, record_target FROM {table_name}"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        yield (row[0], row[1], row[2], row[3], row[4])
    
def delete_data(title):
    global conn, cur    
    sql = f"DELETE FROM {table_name} WHERE title='{title}';"
    print(sql)
    cur.execute(sql)
    conn.commit()

def get_data(column, value):
    global conn, cur
    sql = f"SELECT title, target, owe, now FROM {table_name} WHERE {column}='{value}'"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        return (row[0], row[1], row[2], row[3])

def update_data(title, target, owe, now):
    global conn, cur
    sql = f"UPDATE {table_name} SET target='{target}', owe='{owe}', now='{now}' WHERE title='{title}'"
    cur.execute(sql)
    conn.commit()

def get_date():
    global conn, cur
    sql = f"SELECT date FROM date_table"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        return row[0]

def reset_record(title, owe, now, record_target):
    global conn, cur
    global conn, cur
    sql = f"UPDATE {table_name} SET target='{record_target}', owe='{owe}', now='{now}' WHERE title='{title}'"
    cur.execute(sql)
    conn.commit()


if __name__ == '__main__':
    with DBHandler():
        insert_date()
