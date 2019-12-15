import argparse
import tree

def main():
    parser = argparse.ArgumentParser(description='Poor man\'s python implementation of the tree command')
    parser.add_argument("--L", default=3, type=int, help="Defines the maximum number of levels tree should go down in the hierarchy. '1' means just the direct contents of the folder.")
    args = parser.parse_args()

    source_path = '.'
    maximum_depth = args.L
    depth = 0
    tree.process_files(source_path, source_path, depth, maximum_depth)

main()