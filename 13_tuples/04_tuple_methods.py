# Create a tuple
my_tuple = (10, 20, 30, 40, 50, 20)
print(my_tuple)

# Because tuples are immutable, they dont have many methods like lists do - only two built-in methods

# 1. count() - returns the count of occurrences of the specified element
print("Count of 20:", my_tuple.count(20))

# 2. index() - returns the index of the first occurrence of the specified element
print("Index of 20:", my_tuple.index(20))