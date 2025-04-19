# global keyword is used to modify global variables

def sum(a, b):
    c = a + b
    global z # to modify global variable z
    z = 2 # This will refer to global z and not create a local variable
    return c

z = 10 # Global variable

print(sum(15, 4))
print(z)