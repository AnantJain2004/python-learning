# shutil module - shutil stands for shell utilities. It complements the os module by providing more advanced file operations.

import shutil

# 1. copy("source.txt", "destination.txt") - copy a file
#       ∘ If destination.txt exists, it is overwritten
shutil.copy("demo.txt", "demo2.txt")

# 2. copy2("source.txt", "destination.txt") - copy a file with metadata (timestamps, permissions)
shutil.copy2("demo.txt", "demo3.txt")

# 3. copytree("source_folder", "destination_folder") - copy an entire directory
#       ∘ destination_folder must not already exist
shutil.copytree("dir", "dir_for_shutil")

# 4. move("old_location.txt", "new_location.txt") - move a file or folder
#       ∘ overwrites if the destination exists
shutil.move("demo2.txt", "dir_for_shutil/")

# 5. rmtree("folder") - remove an entire directory
shutil.rmtree("dir_for_shutil")