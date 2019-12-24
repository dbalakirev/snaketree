import os

def bold(text):
    return '\033[1m' + text + '\033[0m'

def format_path_entry(path_name, indent_level):
    divider = '-' * indent_level
    return "{} {} {}".format(divider, path_name, indent_level)

def process_files(dir_name, dir_path, indent_level, maximum_depth):
    found_tree = {}
    if indent_level >= maximum_depth:
        return found_tree

    paths = os.listdir(dir_path)
    for path in paths:
        next_level = indent_level + 1
        real_path = dir_path + '/' + path
        if os.path.isdir(real_path):
            sub_tree = process_files(path, real_path, next_level, maximum_depth)
            found_tree[path] = {}
            found_tree[path].update(sub_tree)
        else:
            # TODO: os.path.isfile would be better to filter out devices
            found_tree[path] = path
    return found_tree