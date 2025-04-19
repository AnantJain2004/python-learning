# Scope - where a variable can be accessed
# Lifetime - how long a variable exists in memory

def sum(a,b): # a and b are local variables
    c = a+b
    z = 1 # It creates a local variable called z which is destroyed when this function returns
    return c

def greet():
    z = 46 # Local variable
    print("Hello!")

z = 8 # z is a global variable
print(f"Value of z before calling the function: {z}")
print(sum(5,6))
print(f"Value of z after calling the function: {z}")
# print(c) # Error : c is not defined outside the function