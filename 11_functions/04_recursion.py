# Fibonacci Sequence:
# Sequence:  0  1  1  2  3  5  8  13  .  .  .
# Series:    0  1  2  3  4  5  6  7   .  .  .


def fib(n):
    # Base Case of recursion (must have to avoid infinite recursion)
    if n < 0:
        return
    else:
        if n==0:
            return n
        elif n==1:
            return n
        else:
            return fib(n-2) + fib(n-1)  # Recursion: a function calling itself
        
n = int(input("Enter a number: "))
print(fib(n))