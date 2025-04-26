# Creating a dictionary
student = {"name": "John", "age": 34, "city": "New York", "gender": "Male"}
print("Original Dictionary:", student)

# 1. copy() - returns a copy of the dictionary
temp = student.copy()
print("\nCopied Dictionary:", temp)

# 2. clear() - removes all the elements from the dictionary
temp.clear()
print("After temp.clear():", temp)

# 3. fromkeys() - returns a dictionary with the specified keys and the specified value(the value for all keys)
keys = ("subject1", "subject2", "subject3")
default_marks = dict.fromkeys(keys, 0)
print("After dict.fromkeys(keys, 0):", default_marks)

# 4. get() - returns the value of the specified key
print("After student.get(name):", student.get("name"))
print("Using get() with missing key:", student.get("grade", "Not found")) # If key doesn't exists, Not Found will be printed

# 5. items() - returns a list containing tuples for each key-value pairs
print("After student.items():", student.items())

# 6. keys() - returns a list of all the keys in the dictionary
print("After student.keys():", student.keys())

# 7. values() - returns a list of all the values in the dictionary
print("After student.values():", student.values())

# 8. pop(x) - removes and returns the element with the specified key
popped_item = student.pop("city")
print("After student.pop(city):", student, "| Popped Item:", popped_item)

# 9. popitem() - removes and returns the last item from the dictionary
popped_item = student.popitem()
print("After student.popitem():", student, "Popped item:", popped_item)

# 10. setdefault() - returns the value of the specified key. If the key doesn't exist: insert the key with the specified value
student.setdefault("grade", "A")
print("After student.setdefault(grade, A):", student)

# 11. update() - updates the dictionary with the specified key-value pairs
student.update({"city": "California"})
print("After student.update():", student)