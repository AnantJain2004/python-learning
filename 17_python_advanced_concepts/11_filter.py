# filter(function, iterable) - the filter() function is used to filter elements from an iterable based on a condition. It returns only the elements for which the function returns True.

def is_greater_than_9(x):
    if x>9:
        return True
    else:
        return False

numbers = [1,2,3,5,65,7,49,56,20,11,5,6,7,1,2,22,100]
# new_numbers = filter(is_greater_than_9, numbers)
new_numbers = filter(lambda x: x>9, numbers)

print(list(new_numbers))