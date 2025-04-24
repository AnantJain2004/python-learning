# Create a list containing the table of 5
table = []

for i in range(1,11): # this for loop will populate the list which was initially empty
    table.append(5*i)

print(table)

# We can write this 5 lines of code in a single line using List Comprehension
table = [5*i for i in range(1,11)]  # List Comprehension
print(table)