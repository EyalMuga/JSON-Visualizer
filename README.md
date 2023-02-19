# JSON Visualizer
JSON Visualizer is a Python script that converts JSON data into a tree structure and visualizes it using Graphviz. It allows you to quickly understand the structure of your JSON data and identify any issues.

# Getting Started
# Dependencies
This script requires the following libraries to be installed:

* Graphviz
* Treelib
# Installing
To install the required libraries, run the following command:

```pip install graphviz treelib```

# Features
Converts JSON data into a tree structure
Visualizes the tree using Graphviz
Supports compact display of single-key dictionaries
Supports custom symbol for nodes that represent lists
Allows you to delete nodes from the tree
Allows you to get the ancestors of a node that contain a keyword

# Functions
create_node(tree, s, counter_byref, verbose, parent_id=None)
This function creates a new node with a label s in the tree object. The counter_byref 
parameter is used to generate a unique identifier for the node.
 The verbose parameter controls whether the function prints information about the node creation to the console. 
 The parent_id parameter specifies the identifier of the parent node, if any. The function returns the identifier of the newly created node.

to_compact_string(o)
This is a utility function that takes a dictionary or list object o and converts it to a compact string representation. 
If o is a dictionary, it is assumed to have only one key-value pair, and the function returns a string in the format "key:value",
where key is the key of the pair and value is the compact string representation of the value. If o is a list, it is assumed to 
have only one element, and the function returns a string in the format "[value]", where value is the compact string representation 
of the element. If o is neither a dictionary nor a list, the function simply returns a string representation of o.

to_compact(tree, o, counter_byref, verbose, parent_id)
This function is used to represent single key-value pairs in a compact form in the tree, rather than creating 
a separate node for each key. It calls to_compact_string on the input o and creates a node in the tree with the resulting 
string as the label, if the string contains only a single key-value pair. The tree, counter_byref, verbose, and parent_id 
parameters have the same meaning as in create_node. The function returns True if a compact node was created, and False otherwise.

json_2_tree(o, parent_id=None, tree=None, counter_byref=[0], verbose=False, compact_single_dict=False, listsNodeSymbol='+')
This function is the main function for converting a JSON object into a tree structure. It takes a JSON object o as input and 
recursively creates nodes in the tree object for each key-value pair or list element. The parent_id parameter specifies the 
identifier of the parent node, if any. If tree is not provided, a new tree object is created. The counter_byref parameter is 
used to generate unique identifiers for the nodes. The verbose parameter controls whether the function prints information about 
the node creation to the console. If compact_single_dict is True, single key-value pairs in the input JSON object are represented 
as compact nodes in the tree, rather than creating a separate node for each key. If listsNodeSymbol is not None, a special node with 
the label specified by listsNodeSymbol is created to represent lists, and each element of the list is added as a child of that node. 
The function returns the tree object.

delete_node(tree, node_id)
This function deletes the node with the specified node_id and all of its descendants from the tree object.

get_ancestors_by_keyword(tree, keyword)
This function searches the tree object for nodes that contain the specified keyword in their label and returns a list of 
the ancestors of those nodes.

visualize_tree(tree)
This function generates a visualization of the tree object using the graphviz library and saves it to a file called code_tree.gv. 
It returns a Digraph object representing the tree

# Example usage
An example to visaulize the json file
<img width="1384" alt="Screenshot 2023-02-16 at 9 00 20" src="https://user-images.githubusercontent.com/117386089/219291644-fbbf4042-b623-4587-8a49-6dce71a08a5e.png">

# Json2tree function example
<img width="290" alt="Screenshot 2023-02-16 at 9 02 39" src="https://user-images.githubusercontent.com/117386089/219292247-99496de9-9b18-4d21-9e21-acb8a11da797.png">

