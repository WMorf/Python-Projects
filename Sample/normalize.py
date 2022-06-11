

def getName():
    '''This is a docstring'''
    fName = input("Please type in your first name without and capitals. \n>>> ").lower()
    print("Thank you {}, Welcome back!".format(fName))
    print(getName.__doc__)

getName()
