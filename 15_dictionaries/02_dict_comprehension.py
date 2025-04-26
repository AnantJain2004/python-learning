# Create a dictionary containing table of 5
my_dict = {}

for i in range(1,11):
    my_dict.update({i: 5*i})

print(my_dict)

# We can write this 5 lines of code in a single line using dictionary comprehension
table = {i: i*5 for i in range(1,11)}
print(table)