# map(function, iterable) - the map() function applies a given function to each and every item in an iterable(like list, tuple, etc.) and returns a map object(which you can convert to a list, tuple, etc.)

def square(x):
    return x*x

numbers = [1, 2, 3, 4, 5]
squares = map(square, numbers)

print(list(squares))

# using map() with a lambda function with multiple iterables
a = [1, 2, 3]
b = [4, 5, 6]

sums = map(lambda x,y: x+y, a, b)

print(list(sums))