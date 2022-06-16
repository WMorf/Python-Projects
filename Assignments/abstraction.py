from abc import ABC, abstractmethod


# parent class
class myAbstractClass(ABC):


    def printName(self, name):
        print('Hello {}, please pick a number'.format(name))

    # abstract method
    @abstractmethod
    def printNum(self, number):
        pass


# child class
class thisChild(myAbstractClass):
    # define parent printNum method
    def printNum(self, number):
        print('The number you''ve selected is {}.'.format(number))


# create object using child of myAbstractClass
obj = thisChild()
obj.printName('Wes')
obj.printNum(5)
