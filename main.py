import json
from functions_tree import *

if __name__ == '__main__':
    import json
    with open('example.json', 'r') as f:
        data = json.load(f)
        tree = json_2_tree(data)
        tree.show()

    print(visualize_tree(tree))