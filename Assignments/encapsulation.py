

class myProtectedClass:
    def __init__(self):
        # single underscore indicates protected
        self._protectedVar = 0
        self.__privateVar = 10

    def getProtected(self):
        print(self._protectedVar)

    def getPrivate(self):
        print(self.__privateVar)

# create object using protected attribute
obj = myProtectedClass()
obj._protectedVar = 50
# prints protectedVar
obj.getProtected()
# gets and prints privateVar
obj.getPrivate()

