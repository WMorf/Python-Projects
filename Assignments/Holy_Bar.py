


greeting = 'The most hopping place in the afterlife is this holy bar \nEverybody wants in.\n\n'

class Soul:
    # sets initial values
    def __init__(self, name, age, entry_status):
        self.name = name
        self.age = age
        self.entry_status = entry_status

    def Enter(self):
        msg = "{} approaches the bar".format(self.name)
        if self.entry_status:
            result = "\nThey get in!\n"
        else:
            result = "\nThey are turned away\n"
        return msg + result

# child class
class Angel(Soul):

    def Enter(self):
        msg = "{} approaches the bar".format(self.name)
        # polymorph altering entry_status
        holy = "\nBright light shines on the guest list..."
        self.entry_status = True
        if self.entry_status:
            result = "\nThey get in!\n"
        else:
            result = "\nThey are turned away\n"
        return msg + holy + result
        

# child class
class Demon(Soul):

    def Enter(self):
        msg = "{} approaches the bar".format(self.name)
        # polymorph altering entry_status
        cheater = "\nThey give a false name..."
        self.entry_status = True
        if self.entry_status:
            result = "\nThey get in!\n"
        else:
            result = "\nThey are turned away\n"
        return msg + cheater + result








































if __name__ == "__main__":

    print(greeting)
    
    # Soul() object
    x1 = Soul('Bob','30',False)
    print(x1.Enter())

    # Angel() object
    x2 = Angel('Uriel','3000',False)
    print(x2.Enter())

    # Demon() object
    x3 = Demon('Crowley','5000',False)
    print(x3.Enter())

