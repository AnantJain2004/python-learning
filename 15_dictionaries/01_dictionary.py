# Dictionary - collection of key-value pairs
#            - each key maps to a value
#            - use curly braces {}

# Creating a dictionary
student = {"name": "Matt", "age": 31, "city": "New York"}
print(student)

# Note - keys must be unique


# Accesing values
print("\nName of student:", student["name"])
# print("Grade of student:", student["grade"]) # Key Error: key doesn't exist

# Safer access - .get()
print("\nName of Student:", student.get("name"))
print("Grade of student:", student.get("grade")) # Output: None (no error)

# Looping through dictionary
print("\n# ---- Looping through dictionary ---- #")
for key, value in student.items():
    print(key, ":", value)

# Adding or Updating the key
print("\n# ---- Adding or Updating the key ---- #")
print("Original Dictionary:", student)

student["grade"] = "A" # Adds new key
print("After adding grade key:", student)

student["age"] = 29 # Updates existing key
print("After updating age:", student)

# Removing Items
print("\n# ---- Removing Items ---- #")
print("Dictionary:", student)

student.pop("city") # Removes "city"
print("After student.pop(\"city\"):", student)

del student["age"] # Also removes "age"
print("After del student[age]:", student)

student.clear() # Clears the entire dictionary
print("After student.clear():", student)