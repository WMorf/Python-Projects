import sqlite3

with sqlite3.connect('C:/Users/clerk/Documents/GitHub/Python-Projects/test4.db') as connection:
    c = connection.cursor()
    c.executescript("""DROP TABLE IF EXISTS People;
                    CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
                    INSERT INTO People VALUES('Ron', 'Obvious', '42');
                    """)

firstName = input("Enter first name: ")
lastName = input("Enter last name: ")
age = int(input("Enter your age: "))

with sqlite3.connect('test4.db') as connection:
    c = connection.cursor()
    line = "INSERT INTO People VALUES ('"+ firstName +"', '"+ lastName +"', " +str(age) +")"
    c.execute(line)
    print(line)
