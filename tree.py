import os

# requirements
# 1. print local tree structure
# 2. print to a certain level
# 3. print the give path

source_path = '.'

files = os.listdir(source_path)
for path in files:
    if os.path.isdir(path):
        print("dir: ", path)
    elif os.path.isfile(path):
        print("file: ", path)

