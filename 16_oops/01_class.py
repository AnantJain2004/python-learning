# class: ● a class is a template or blueprint to create objects
#        ● it defines what an object will be like - what data it will hold and what actions it can perform
#        ● Eg - think of a class like a car design, it doesn't do anything but tells how to build a car

# object: ● an object is a specific instance created from the class
#         ● each object has its own unique set of data
#         ● Eg - if "Car" is the class, then the real car is an object created from the "Car" class

class Employee:
    company = "DELL"

    def get_salary(self): # self is a reference to the current object of the class that is being created or used  
        return 35000
    
e1 = Employee() # An object of class "Employee" is created here
print(e1.company)
print(e1.get_salary())

e2 = Employee()
print(e2.company)
print(e2.get_salary())

# Note: it's mandatory to give first parameter as self for all the functions that are defined inside the class