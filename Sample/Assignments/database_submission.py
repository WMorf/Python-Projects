
import sqlite3




# creates database if none exists already, then connects to it
conn = sqlite3.connect('afile.db')

# While connected:
with conn:
    cur = conn.cursor()
    # creates table if none exists already 
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname varchar(255) \
        )")
    # saves changes to DB
    conn.commit()
conn.close()


# tuple to be sorted
fileList = ('information.dox','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

fileload = []

# sort fileList for values containing .txt and add them to new list
for i in fileList:
    if ".txt" in i:
        fileload.append(i)

conn = sqlite3.connect('afile.db')

# insert into table
with conn:
    cur = conn.cursor()
    # loop inserts files
    for i in fileload:
        file = i
        cur.execute("INSERT INTO tbl_files(col_fname) VALUES (?)", (file,))
        conn.commit()
        print("{} \nsuccesfully added to database!".format(i))
conn.close()

