# reduce(function, iterable<, initializer>): reduce() function reduces a sequence of values into a single value by repeatedly applying a binary function.
# ● it's part of the functools module

from functools import reduce

def sum(a, b):
    return a+b

numbers = [1,2,3,4,5,6]
#         [3,3,4,5,6]
#         [6,4,5,6]
#         [10,5,6]
#         [15,6]
#         [21]

sum_value = reduce(sum, numbers)
print(sum_value)