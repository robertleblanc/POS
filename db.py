import sqlite3


class Database:
    def __init__(self):
        self.STUDENT_TBL = 'students'
        self.DATABASE = 'data.db'

    def connect(self):
        con = None
        try:
            con = sqlite3.connect(self.DATABASE)
        except sqlite3.Error as e:
            print(e)
        return con

    def read_all(self):
        with self.connect() as con:
            sql = f'SELECT * FROM {self.STUDENT_TBL}'
            rows = con.execute(sql)
            return rows
        con.close()
