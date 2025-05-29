# os module - it's used for interacting with the OS
# It allows Python Programs to:
#       ● create, delete, rename files and folders
#       ● work with paths
#       ● get system-related info
#       ● execute system-level commands

import os

# 1. getcwd() - Get current working directory
print("Before changing:", os.getcwd())

# 2. chdir() - Change current directory
os.chdir(r"C:\Users\Anant_Jain\OneDrive\Desktop\Python Course")

# Print current directory again to confirm change
print("After changing:", os.getcwd())

# 3. listdir() - list files and folders in a directory
print(os.listdir()) # list files and folders in current directory
print(os.listdir("dir")) # list files and folders in specified path

# 4. mkdir() - make a new directory
os.mkdir("sample_folder")

# 5. mkdirs() - make multiple nested directories
os.makedirs("parent\child\grandchild")

# 6. rmdir() - remove a directory (if empty)
os.rmdir("sample_folder")

# 7. removedirs() - removes all specified directories (if empty)
os.removedirs("parent\child\grandchild")

# File Handling with OS
# check if a file or directory exists
print(os.path.exists("demo.txt")) # True / False
print(os.path.isfile("sample1.txt")) # True if file
print(os.path.isdir("dir")) # True if directory

# 8. rename() - Rename a file
os.rename("old.txt", "new.txt")

# 9. remove() - Delete a file
os.remove("new.txt")