try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"The division is {a/b}")
except Exception as e:
    print(e)
else: # Gets executed when there is no error in the try block
    print("Hey, I am good")