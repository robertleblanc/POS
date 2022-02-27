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

    def test(self):
        print("IT worked!")

    def read_all(self):
        with self.connect() as con:
            sql = f'''SELECT
                id,
                last,
                first,
                rfid,
                balance
            FROM {self.STUDENT_TBL}'''
            rows = con.execute(sql)
            return rows
        con.close()

    def insert_new_record(self, _values):
        with self.connect() as con:
            sql = f'''INSERT INTO
                {self.STUDENT_TBL}
                (last, first, rfid, balance)
                VALUES(
                    :last,
                    :first,
                    :rfid,
                    :balance
                )'''
            con.execute(sql, _values)
        con.close()

    def update_by_id(self, _id, _data):
        with self.connect() as con:
            sql = f'''UPDATE {self.STUDENT_TBL}
                SET
                    last = :last,
                    first = :first,
                    rfid = :rfid,
                    balance = :balance
                WHERE
                    id = {_id}'''

            con.execute(sql, _data)
        con.close()
