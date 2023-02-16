# JSON-Visualizer
The code in this project provides functions for converting a JSON object into a tree structure and visualizing the
resulting tree using Graphviz. The main functions are json_2_tree and visualize_tree.
Here is a brief overview of each function:

# create_node: creates a node in the tree with the given string label and a unique numerical identifier.
The function also increments a counter to keep track of the number of nodes in the tree.

# to_compact_string: recursively converts a JSON object to a compact string representation.
This function is used by json_2_tree to represent single-key dictionaries as a single node in the tree.

# to_compact: converts a JSON object to a compact string representation using to_compact_string,
and then creates a single node in the tree with that string as its label.
This function is used by json_2_tree to represent single-key dictionaries as a single node in the tree.

# json_2_tree: recursively converts a JSON object to a tree structure using the create_node and to_compact functions.
This function creates a new node in the tree for each key-value pair in a dictionary and each element in a list. 
It also uses the to_compact function to represent single-key dictionaries as a single node in the tree.

# delete_node: removes a node from the tree and all its children.

# visualize_tree: creates a Digraph object from the tree and renders it using Graphviz.
The resulting visualization is saved to a file named "code_tree.gv". The visualization is also displayed in a window,
if view=True is passed to the function.

