class name:
    def __init__(self, firstName, lastName):
        #Initializing values for future objects created from this class
        self.firstName=firstName
        self.lastName=lastName
    def printName(self):
        print("Hello, I am {} {}".format(self.firstName, self.lastName))

#Passing in the actual object values
person=name('Dustin', 'Smith')
person.printName()
