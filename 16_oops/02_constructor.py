# Constructor: ● A special method(__init__) in a class that runs automatically when you create an object
#              ● It is used to initialize the object's attribute with some intial values

# Define a class
class Student:
    # Constructor method
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    # Method to display student info
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")

    # Method to check pass/fail
    def is_passed(self):
        if self.grade >= 50:
            print("Status: Passed")
        else:
            print("Status: Failed")

# Ask for user input
name = input("Enter student's name: ")
age = int(input("Enter student's age: "))
grade = int(input("Enter student's grade: "))

# Create an object
student1 = Student(name, age, grade)

# Use the object's method
student1.display_info()
student1.is_passed()