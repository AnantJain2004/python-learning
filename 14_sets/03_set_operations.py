# ---- Set Operations ---- #
print("\n# ---- Set Operations ---- #")

# Creating two sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Set a:", a)
print("Set b:", b)

# 1. union - set of elements that belong to set A or set B, or both
print("\na.union(b):", a.union(b))

# 2. intersection - set of elements that belong to both set A and set B
print("a.intersection(b):", a.intersection(b))

# 3. difference - set containing elements that are in A but not in B
print("a.difference(b):", a.difference(b))

# 4. symmetric_difference - set containing elements that are in A or B but not in both
print("a.symmetric_difference(b):", a.symmetric_difference(b))

# ---- Check Methods ---- #
print("\n# ---- Check Methods ---- #")

# Creating two sets
x = {3, 4}
y = {10, 11}

print("\nX:", x)
print("Y:", y)

print("x.issubset(a):", x.issubset(a))
print("a.issuperset(x):", a.issuperset(x))
print("x.isdisjoint(y):", x.isdisjoint(y))