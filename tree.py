import os

def bold(text):
    return '\033[1m' + text + '\033[0m'

def print_file_name(dir_name, indent_level):
    divider = '-'
    print(divider * indent_level, dir_name, indent_level)

def process_files(dir_name, dir_path, indent_level, maximum_depth):
    if indent_level >= maximum_depth:
        return
    print_file_name(bold(dir_name), indent_level)
    paths = os.listdir(dir_path)
    for path in paths:
        real_path = dir_path + '/' + path
        if os.path.isdir(real_path):
            process_files(path, real_path, indent_level + 1, maximum_depth)
        else:
            # TODO: os.path.isfile would be better to filter out devices
            print_file_name(path, indent_level + 1)