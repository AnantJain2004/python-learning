file = open("demo.txt", "r")

for line in file:
    print(line.strip()) # strip() - remove new line characters

file.close()