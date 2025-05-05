# Note - ● by default, a method inside a class is an instance method.
#        ● we write static methods whenever we don't want any association with the instance attributes.

class Employee:
    company = "Lenovo"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Instance method - default methods that we create within a class
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}."
        print(info)

    # Static Method
    @staticmethod
    def sum(a ,b):
        return a+b

e1 = Employee("Jack", 35000)
e2 = Employee("Alan", 47000)

print(Employee.company)
# print(Employee.name) # it will throw an error
e1.print_info()
e2.print_info()

print(e2.sum(32, 78))