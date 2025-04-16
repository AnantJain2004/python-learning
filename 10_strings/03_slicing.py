text = "Anant0123456789" # Length = 15

#  A   n   a   n   t   0   1   2   3   4   5   6   7   8   9
#  0   1   2   3   4   5   6   7   8   9   10  11  12  13  14

# By default: start = 0, stop = length of the string, step = 1

print(text[2:5])
print(text[:5]) # Same as text[0:5]
print(text[:])
print(text[5:])
print(text[5:-3]) # Same as text[5:12]
print(text[::2])
print(text[-1:-4:-1]) # we have to give -ve step value
print(text[::-1]) # Reverse the string