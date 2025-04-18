# Arguments(actual parameters) -> are the values or variables that are passed to a function when calling it
# Parameters(Formal parameters) -> are the variables that are listed in the function definition that receives the values of the actual parameters

# Positional Arguments
def sum(a,b):
    return a+b
print(f"Sum = {sum(5,3)}")


# Default Arguments
def multiply(a,b,c=2):
    return a*b*c
print(f"Multiplication = {multiply(5,3)}") # 5*3*2
print(f"Multiplication = {multiply(5,3,1)}") # 5*3*1 (c = 2 will be overridden)


# Keyword Arguments
def subtract(a,b):
    return a-b
print(f"Subtraction: {subtract(b=3,a=6)}") # 6 - 3 = 3