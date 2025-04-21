# Create a list
mylist = [3, 1, 4, 1, 5]
print("Original list:", mylist)

# append() - Add to the end
mylist.append(9)
print("After append(9):", mylist)

# insert() - Insert at a specific index
mylist.insert(2, 7)
print("After insert(2, 7):", mylist)

# extend() - Add multiple items
mylist.extend([10, 11])
print("After extend([10, 11]):", mylist)

# remove() - Remove first occurrence of a value
mylist.remove(1)
print("After remove(1):", mylist)

# pop() - Remove and return last item
popped = mylist.pop()
print("After pop():", mylist, "| Popped:", popped)

# pop(index) - Remove and return item at index
popped_index = mylist.pop(0)
print("After pop(0):", mylist, "| Popped index 0:", popped_index)

# index() - Get index of value
idx = mylist.index(4)
print("Index of 4:", idx)

# count() - Count how many times a value appears
count_1 = mylist.count(1)
print("Count of 1:", count_1)

# copy() - Make a copy of the list
copied_list = mylist.copy()
print("Copied list:", copied_list)

# sort() - Sort the list
mylist.sort()
print("After sort():", mylist)

# reverse() - Reverse the list
mylist.reverse()
print("After reverse():", mylist)

# clear() - Remove all items from the list
mylist.clear()
print("After clear():", mylist)
