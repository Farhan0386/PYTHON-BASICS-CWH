import os

# Specify the directory you want to list (use '.' for current directory)
directory = '.'

# Get the list of files and directories
contents = os.listdir(directory)

# Print each item
for item in contents:
    print(item)