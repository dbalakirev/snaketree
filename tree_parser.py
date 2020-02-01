def tree_to_string(tree, level=0):
    result = []
    if level == 0:
        result.append(".")
    length = len(tree.keys())
    i = 0
    for key in tree.keys():
        if i == length - 1:
            result.append("\n\u2514")
        else:
            result.append("\n\u251c")
        dash = "\u2500"
        result.append(f'{"":{dash}<{level}} {key}')
        if type(tree[key]) is dict:
            sub_tree = tree_to_string(tree[key], level=level+1)
            result.append(sub_tree)
        i += 1
    return "".join(result)
    #"." + "\n" + "├── .vscode" + "\n" + "│   └── file.txt" + "\n" + "└── settings.json"