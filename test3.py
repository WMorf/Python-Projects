
import sqlite3

# creates database if none exists already, then connects to it
conn = sqlite3.connect('test.db')

# While connected:
with conn:
    cur = conn.cursor()
    # creates table if none exists already 
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_lname TEXT \
        )")
    # saves changes to DB
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

# insert into table
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname) VALUES (?,?)", \
                ('Tob','Smith'))
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname, col_lname FROM tbl_persons WHERE col_fname = 'Tob'")
    # store selected records in variable
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "First Name: {}\nLast Name: {}".format(item[0],item[1])
    print(msg)

