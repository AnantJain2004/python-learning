# function -> reusable block of code that performs a specific task

# A greeting function
def greet():        # fn definition
    print("Hi there!")

greet()     # fn calling

# function with parameters(no return value)
def calculate_avg(a, b, c):
    d = (a+b+c)/3
    print(f"Average = {d}")

calculate_avg(5,3,2)

# function with parameters(with return value)
def calculate_sum(a, b, c):
    result = a+b+c
    return result

sum = calculate_sum(5,3,4)
print(f"Sum = {sum}")