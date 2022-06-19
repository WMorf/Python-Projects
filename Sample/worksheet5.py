import sqlite3

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
personData = (firstName, lastName, age)

with sqlite3.connect('test4.db') as connection:
    c = connection.cursor()
    c.execute("INSERT INTO People VALUES(?, ?, ?)", personData)

c.execute("UPDATE People SET AGE=? WHERE FirstName=? AND LastName=?",
          (45, 'Ron', 'Obvious'))
