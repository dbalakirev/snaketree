import argparse
import tree

def main():
    parser = argparse.ArgumentParser(description='Poor man\'s python implementation of the tree command')
    parser.add_argument("-d", "--directory", default='.', type=str, help="The directory to discover")
    parser.add_argument("-L", "--maximum_level", default=3, type=int, help="Defines the maximum number of levels tree should go down in the hierarchy. '1' means just the direct contents of the folder.")
    args = parser.parse_args()

    source_path = args.directory
    maximum_depth = args.maximum_level
    depth = 0
    found_paths = tree.process_files(source_path, source_path, depth, maximum_depth)
    print("{} directories, {} files".format(found_paths[0], found_paths[1]))

main()