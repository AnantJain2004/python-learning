# Instance attributes: ● belong to each object separately
#                      ● defined inside __inti__() method
#                      ● can have different values for each object

# Class attributes: ● are shared by all objects of the class
#                   ● defined outside any method
#                   ● are same for every object

class Dog():
    species = "Canine" # Class attribute

    def __init__(self, name, breed):
        self.name = name # I
        self.breed = breed

dog1 = Dog("Bruno", "Labrador")
dog2 = Dog("Tommy", "Husky")

print(f"1. Dog name: {dog1.name}, Dog breed: {dog1.breed}, Dog species: {Dog.species}")
print(f"2. Dog name: {dog2.name}, Dog breed: {dog2.breed}, Dog species: {dog2.species}")