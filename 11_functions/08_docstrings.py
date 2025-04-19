# Docstring -> special string that you write inside a function, class, or module to describe what it does
# Docstrings are written right after starting the function to attach information to a function

def add(a, b):
    """
    Returns the sum of two numbers

    Parameters:
    a (int) : The first number
    b (int) : The second number

    Returns:
    int : The sum of two numbers
    """
    return a+b

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

print(f"Sum of {a} and {b} = {add(a,b)}")
print(add.__doc__)