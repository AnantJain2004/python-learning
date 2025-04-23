# Create a list
mylist = [3, 1, 4, 1, 5]
print("Original list:", mylist)

# 1. append() - adds an element at the end of the list
mylist.append(9)
print("After append(9):", mylist)

# 2. insert() - adds an element at the specified index
mylist.insert(2, 7)
print("After insert(2, 7):", mylist)

# 3. extend() - add the elements of a list at the end of the current list
mylist.extend([10, 11])
print("After extend([10, 11]):", mylist)

# 4. remove() - removes the first occurrence of the specified element
mylist.remove(1)
print("After remove(1):", mylist)

# 5. pop() - removes the element at the specified index(by default, last) and returns it
popped = mylist.pop()
print("After pop():", mylist, "| Popped:", popped)

# 6. pop(index)
popped_index = mylist.pop(0)
print("After pop(0):", mylist, "| Popped index 0:", popped_index)

# 7. index() - returns index of the first occurrence of the specified element
idx = mylist.index(4)
print("Index of 4:", idx)

# 8. count() - returns the count of the specified element
count_1 = mylist.count(1)
print("Count of 1:", count_1)

# 9. copy() - returns a copy of the list
copied_list = mylist.copy()
print("Copied list:", copied_list)

# 10. sort() - sorts the list
mylist.sort()
print("After sort():", mylist)

# 11. reverse() - reverses the order of the list
mylist.reverse()
print("After reverse():", mylist)

# 12. clear() - removes all the elements from the list
mylist.clear()
print("After clear():", mylist)