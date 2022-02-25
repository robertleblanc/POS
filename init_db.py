import sqlite3 as sq
import csv
import sys
from pathlib import Path

# Running this script will create 'data.db' and populate it with the students
# found in 'students.csv' - it should be smart enough to only run once
STUDENT_TBL = 'students'
DATABASE = 'data.db'

# Check to see if the database already exists. Exit if it exists
path = Path(DATABASE)
if path.is_file():
    sys.exit(f"{DATABASE} already exists - quiting...")


CREATE_STUDENTS_TABLE_SQL = f"""CREATE TABLE IF NOT EXISTS {STUDENT_TBL} (
    id INTEGER PRIMARY KEY,
    first TEXT,
    last TEXT,
    rfid INTEGER,
    balance REAL
)"""

INSERT_STUDENT_SQL = f"""INSERT INTO {STUDENT_TBL}
    (last, first, rfid, balance) VALUES
    (?,?,?,?)"""

# Using a context manager ie. 'with' on connection will automatically commit
# or rollback transactions. It will not close the connection
con = sq.connect(DATABASE)

try:
    with con:
        con.execute(CREATE_STUDENTS_TABLE_SQL)
except sq.OperationalError as e:
    print("Error creating table:", e)
    sys.exit("Exit program")

# Read initialization data from csv file
with open('students.csv') as students_file:
    csvreader = csv.reader(students_file)
    # take each line in csv and map it into a list of tuples
    entries = list(map(tuple, csvreader))

with con:
    try:
        con.executemany(INSERT_STUDENT_SQL, entries)
    except Exception as e:
        print(e)

con.close()
