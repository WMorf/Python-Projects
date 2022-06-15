

# parent class
class LifeForm:
    name = "?"
    species = "?"
    legs = None
    arms = None
    dna = "Sequence A"
    origin = "?"
    carbon_based = True

    def information(self):
        msg = "\nName: {}\nSpecies {}\nLegs: {}\nArms: {}\nDNA {}\nOrigin {}\nCarbon Based: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg
        
# child class instance
class Human(LifeForm):
    name = "Steve"
    species = "Homesapien"
    legs = 2
    arms = 2
    dna = "Sequence A"
    origin = "Earth"

    def ingenuity(self):
        msg = "\nLives on the moon to avoid crimes"
        return msg

# another child class instance
class Dog(LifeForm):
          name = "Dug"
          species = "Canine"
          legs = 4
          arms = 0
          dna = "Sequence B"
          origin = "Earth"

          def bite(self):
              msg = "/n growls and bites target"
              return msg


if __name__ == "__main__":
    human = Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bite())
