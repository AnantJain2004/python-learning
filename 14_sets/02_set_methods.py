# Creating two sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Set A:", a)
print("Set B:", b)

# 1. add() - adds an element to the set
a.add(7)
print("\nAfter a.add(7):", a)

# 2. remove() - removes an element from the set
a.remove(2)
print("After a.remove(2):", a)

# 3. discard() - removes an element from the set (no error if not found)
a.discard(100)
print("After a.discard(100):", a)

# 4. pop() - removes and returns a random element from the set
popped_item = a.pop()
print("After a.pop():", a, "| Popped item:", popped_item)

# 5. update() - add the elements of a set in the current set
a.update(b)
print("After a.update(b):", a)

# 6. copy() - returns a copy of the set
temp = a.copy()
print("Copied set:", temp)

# 7. clear() - removes all the elements from the set
temp.clear()
print("After clear():", temp)