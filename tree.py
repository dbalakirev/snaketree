import os

# requirements
# 1. print local tree structure
# 2. print to a certain level
# 3. print the give path

def print_dir_name(dir_name, indent_level):
    print(' ', dir_name.expandtabs(indent_level), indent_level)

def print_dir(dir_name, dir_path, indent_level):
    # print("debug: ", dir_name, " ", dir_path)
    print_dir_name(dir_name, indent_level)
    paths = os.listdir(dir_path)
    # print("debug: ", paths)
    for path in paths:
        # print("debug: ", path)
        if os.path.isdir(path):
            print_dir(path+"_d", path, indent_level + 1)
        else:
            # TODO: os.path.isfile would be better to filter out devices
            print_dir_name(path, indent_level + 1)

def main():
    source_path = '.'
    indent_level = 1
    print_dir(source_path, source_path, indent_level)

main()