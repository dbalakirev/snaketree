def tree_to_string(tree, root=True):
    result = []
    if root:
        result.append(".")
    for key in tree.keys():
        result.append("\n\u251c")
        result.append(key)
        # If directory
        if type(tree[key]) is dict:
            sub_tree = tree_to_string(tree[key], False)
            result.append(sub_tree)
    return "".join(result)
    #"." + "\n" + "├── .vscode" + "\n" + "│   └── file.txt" + "\n" + "└── settings.json"