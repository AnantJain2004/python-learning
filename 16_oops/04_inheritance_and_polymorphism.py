# Inheritence - ● A child class (or subclass) inherits the attributes and methods from its parent class
#                 (or superclass)
#               ● This allows you to create new classes that are specialized versions of existing classes,
#                 without rewriting all the code

# super() - inside a child class, super() lets you call methods from the parent class

class Animal: # Parent class (superclass)

    location = "Australia"

    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("Generic animal sound")

class Dog(Animal): # Dog inherits from Animal (Dog is a subclass)
    def speak(self): # We override the speak() method
        super().speak() # We are using the speak method of parent class
        print("Woof!")

class Cat(Animal): # Cat also inherits from Animal
    def speak(self):
        print("Meow!")

# Create objects
my_dog = Dog("Bruno")
my_cat = Cat("Fluffy")

# They both have a 'name' attribute (inherited from animal)
print(my_dog.name)
print(my_cat.name)

# They both a 'speak()' method, but it behaves differently
my_dog.speak()
my_cat.speak()