def divide(a, b):
    try:
        c = a/b
        print(f"The division is {a/b}")
    except Exception as e:
        print(e)
    
    finally: # this is always executed no matter if there is any error in the try block or not
        print("This is always executed")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
divide(a, b)