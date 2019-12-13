import os

# requirements
# 1. print local tree structure
# 2. print to a certain level
# 3. print the give path

def print_dir_name(dir_name, indent_level):
    print(' ', dir_name.expandtabs(indent_level), indent_level)

def print_dir(dir_name, dir_path, indent_level):
    print_dir_name(dir_name, indent_level)
    paths = os.listdir(dir_path)
    for path in paths:
        if os.path.isdir(path):
            print_dir(path, path, indent_level + 1)
        elif os.path.isfile(path):
            print_dir_name(path, indent_level + 1)

def main():
    source_path = '.'
    indent_level = 1
    print_dir(source_path, source_path, indent_level)

main()