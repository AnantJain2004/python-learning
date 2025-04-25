# Set - unordered, unique collection of elements
#     - uses curly braces{} or the set() constructor
#     - no duplicate values
#     - no indexing(because sets are unordered)

# Creating a set
my_set = {1,2,3,4,5}
print(my_set)

# Set with duplicate elements
my_set2 = {10,20,20,30,30,30,40,50}
print(my_set2)

# Creating a set from a list
my_list = [11,23,45,67,21,45]
list_to_set = set(my_list)
print(list_to_set)