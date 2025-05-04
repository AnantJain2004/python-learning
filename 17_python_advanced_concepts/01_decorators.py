# Decorator: ● a decorator is a function that wraps additional functionality around an existing function without changing its actual code
#            ● it takes a function as an argument, then it creates a new function(wrapper()) inside its body and then it returns that new funtion

def decorator(func):
    def wrapper():
        print("Hello!")
        func()
        print("Goodbye!")
    return wrapper

@decorator
def say_name():
    print("My name is Anant.")
# This is just a shortcut for:
# f = decorator(say_name)
# f()

say_name()