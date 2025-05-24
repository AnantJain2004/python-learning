# ● Magic methods, also called dunder methods, have double underscores at the beginning and at the end of
#   their name.
# ● These methods allow you to define how your objects interact with built-in Python operators and fns.
# ● They are used to:
#   ∘ Customize object creation and initialization(__init__, __new__)
#   ∘ Implement operator overloading(eg, +,-,*,/,==)
#   ∘ Provide string representation of objects(__str__, __repr__)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __str__(self):
        return f"The name is {self.name} and the salary is {self.salary}"
    
    def __repr__(self):
        return f"Name: {self.name}\nSalary: {self.salary}"
    
    def __len__(self):
        return len(self.name)
    
e = Employee("Anant", 40500)
print(e.name, e.salary)
print(str(e))
print(e)
print(repr(e))
print(len(e))