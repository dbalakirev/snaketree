import os

def bold(text):
    return '\033[1m' + text + '\033[0m'

def format_path_entry(path_name, indent_level):
    divider = '-' * indent_level
    return "{} {} {}".format(divider, path_name, indent_level)

def process_files(dir_name, dir_path, indent_level, maximum_depth):
    if indent_level >= maximum_depth:
        return
    dir_path_entry = format_path_entry(bold(dir_name), indent_level)
    print(dir_path_entry)
    paths = os.listdir(dir_path)
    for path in paths:
        real_path = dir_path + '/' + path
        if os.path.isdir(real_path):
            process_files(path, real_path, indent_level + 1, maximum_depth)
        else:
            # TODO: os.path.isfile would be better to filter out devices
            file_path_entry = format_path_entry(path, indent_level + 1)
            print(file_path_entry)