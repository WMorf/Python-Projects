import sqlite3
from sqlite3 import *

#def Create_Connection():
    #conn = sqlite3.connect(':memory:')

peopleValues = (('Jean-Baptiste_Zorg', 'Human', 122), ('Korben_Dallas', 'Meat-Popsicle', 100), ('Ak''not', 'Manglore', -5))

with sqlite3.connect('test4.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People(Name TEXT, Species TEXT, IQ INT)")
    c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)

    c.execute("SELECT Name, Species, IQ FROM People")
    for row in c.fetchall():
        print(row)

    c.execute("UPDATE People SET Species = 'Human' WHERE Name = 'Korben_Dallas'")

    print("Humans")
    c.execute("SELECT Name, Species, IQ FROM People WHERE Species = 'Human'")
    for row in c.fetchall():
        print(row)





























#if __name__ == "__main__":
    
