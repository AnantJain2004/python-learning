# *args and **kwargs are very important in python, especially when working with functions that accept a variable number of arguments
# ● *args - Variable Positional Arguments
#           ∘ it lets you pass any number of positional arguments to a function
#           ∘ internally args is a tuple of the arguments

def sum(*args):
    print(args) # args = (7,9,4)
    total = 0
    for item in args:
        total += item
    return total
 
print(sum(7,9,4))