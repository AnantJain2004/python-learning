f = open("demo.txt", "r")
content = f.read() # this reads the entire file as a single string.
print(content)
f.close()