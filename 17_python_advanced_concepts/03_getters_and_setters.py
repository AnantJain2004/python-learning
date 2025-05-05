# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     # to return first name
#     def first_name(self):
#         return self.name.split(" ")[0]
    
#     # to change first name
#     def change_first_name(self, first):
#         l = self.name.split(" ")
#         new_name = f"{first} {l[1]}"
#         self.name = new_name


# e = Employee("John Doe", 35000)
# print(e.name)
# print(e.first_name())
# e.change_first_name("Alan")
# print(e.name)

#---------------------------------#
# Getter - a method used to get/retrieve the value of a private attribute
# Setter - a method used to set/update the value of a private attribute

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # to return first name
    @property # Turns a method into an attribute-like getter
    def first_name(self):
        return self.name.split(" ")[0]
    
    # to change first name
    @first_name.setter # Defines the setter for a @property
    def first_name(self, first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name


e = Employee("John Doe", 35000)

print(e.name)
print(e.first_name)
e.first_name = "Alan"
print(e.name)