# Note - ● by default, a method inside a class is an instance method.
#        ● we write static methods whenever we don't want any association with the instance attributes.

class Employee:
    company = "Lenovo"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Instance method - work on objects(instances) of a class
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}."
        print(info)

    # Static Method - ● a helper method, that does not need access to object(self) or class(cls)
    #                 ● used when a method relates to the class logically but doesn't need its data
    @staticmethod
    def sum(a ,b):
        return a+b
    
    # Class Method - works on the class itself, not on objects
    @classmethod
    def print_company(cls):
        print(cls.company)

    # to change company name
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

e1 = Employee("Jack", 35000)
e2 = Employee("Alan", 47000)

print(Employee.company)
# print(Employee.name) # it will throw an error
e1.print_info()
e2.print_info()

print(Employee.sum(32, 78))

# Employee.print_company()
# Employee.change_company("DELL")
# Employee.print_company()

print(Employee.company)
Employee.change_company("DELL")
print(Employee.company)