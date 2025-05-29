# 'a' (Append mode) - If the file exists, the data will be added to the end of the file. If the file doesn't exist, a new file will be created 

f = open("write into this.txt", "a")

content = '''
I want to be a Data Scientist
'''

f.write(content)

f.close()