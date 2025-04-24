# Tuple unpacking lets you assign values to variables directly from a tuple in a single line

person = ("Matt", 33, "New York")
name, age, city = person
print(f"Name: {name}\nAge: {age}\nCity: {city}")

print("\n")

# Use _ to ignore values
person = ("John", 34, "California")
name, _, city = person
print(f"Name: {name}\nCity: {city}")

print("\n")

# tuple unpacking in loops
points = [(1, 2), (3, 4), (5, 6)]

for x, y in points:
    print(f"x: {x}, y: {y}")

print("\n")
print("Swapping")
# Swapping
a, b = 10, 5
print(f"Before swapping: a={a}, b={b}")
a,b = b, a
print(f"After swapping: a={a}, b={b}")