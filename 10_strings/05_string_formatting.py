# .format() -> it is used to insert values into a string by using placeholders {}
name = "Jack"
age = 30
print("My name is {} and I am {} years old.".format(name,age))

# We can also specify positional and keyword arguments
print("{1} is learning {0}.".format("Python","Jack"))
print("{name} is {age} years old.".format(name = "Matt", age = "29"))

print("\n")

# f-strings -> let you embed variables or expressions directly inside a string using {}
name = "Jack"
age = 30
print(f"My name is {name} and I am {age} years old.")

# You can even perform calculations directly inside f-strings
a = 5
b = 3
print(f"The sum of {a} and {b} is {a + b}")

# Formatting Numbers
pi =3.14159265
print(f"Pi rounded to 2 decimal places: {pi:.2f}")

# Padding and Alignment
text = "Python"
print(f"{text:>10}") # right align
print(f"{text:<10}") # left align
print(f"{text:^10}") # center align