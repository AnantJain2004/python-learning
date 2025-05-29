# 'w' (Write mode) - If the file exists, it will be overwritten. If the file doesn't exist, a new file will be created 

f = open("write into this.txt", "w")

content = '''
Hey there, this is Anant and I love writing code in Python.
I work with NumPy and Pandas
'''

f.write(content)

f.close()