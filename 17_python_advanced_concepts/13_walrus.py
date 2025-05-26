# walrus operator: the walrus operator(:=) is used to assign a value to a variable inside an expression
# It allows you to:
#   ∘ Assign and use a variable in a single expression
#   ∘ Make your code shorter and more readable


# Assign inside a condition

# (Tradiitonal approach)
# length = len("Python")
# if(length > 5):
#     print(f"Length is {length}")

# (with walrus)
if (length := len("Python")) > 5:
    print(f"Length is {length}")

# Using in a while loop
# (traditional approach)
# data = input("Enter text: ")
# while(data != "exit"):
#     print(f"You typed: {data}")
#     data = input("Enter text: ")

# (with walrus)
while (data := input("Enter text: ")) != "exit":
    print(f"You typed: {data}")