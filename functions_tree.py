from graphviz import Digraph
from treelib import Node, Tree, node


def create_node(tree, s, counter_byref, verbose, parent_id=None):
    node_id = counter_byref[0]
    if verbose:
        print(f"tree.create_node({s}, {node_id}, parent={parent_id})")
    tree.create_node(s, node_id, parent=parent_id)
    counter_byref[0] += 1
    return node_id

def to_compact_string(o):
    if type(o) == dict:
        if len(o)>1:
            raise Exception()
        k,v =next(iter(o.items()))
        return f'{k}:{to_compact_string(v)}'
    elif type(o) == list:
        if len(o)>1:
            raise Exception()
        return f'[{to_compact_string(next(iter(o)))}]'
    else:
        return str(o)

def to_compact(tree, o, counter_byref, verbose, parent_id):
    try:
        s = to_compact_string(o)
        if verbose:
            print(f"# to_compact({o}) ==> [{s}]")
        create_node(tree, s, counter_byref, verbose, parent_id=parent_id)
        return True
    except:
        return False
    
# convert json to tree
def json_2_tree(o , parent_id=None, tree=None, counter_byref=[0], verbose=False, compact_single_dict=False, listsNodeSymbol='+'):
    if tree is None:
        tree = Tree()
        parent_id = create_node(tree, '+', counter_byref, verbose)
    if compact_single_dict and to_compact(tree, o, counter_byref, verbose, parent_id):
        pass
    # checks if o is a dict
    elif type(o) == dict:
        for k,v in o.items():
            if compact_single_dict and to_compact(tree, {k:v}, counter_byref, verbose, parent_id):
                continue
            key_nd_id = create_node(tree, str(k), counter_byref, verbose, parent_id=parent_id)
            if verbose:
                print(f"# json_2_tree({v})")
            json_2_tree(v , parent_id=key_nd_id, tree=tree, counter_byref=counter_byref, verbose=verbose, listsNodeSymbol=listsNodeSymbol, compact_single_dict=compact_single_dict)
    elif type(o) == list:
        if listsNodeSymbol is not None:
            parent_id = create_node(tree, listsNodeSymbol, counter_byref, verbose, parent_id=parent_id)
        for i in o:
            # checks if i is a dict
            if compact_single_dict and to_compact(tree, i, counter_byref, verbose, parent_id):
                continue
            if verbose:
                print(f"# json_2_tree({i})")
            # recursive call to json_2_tree function for each element in the list  
            json_2_tree(i , parent_id=parent_id, tree=tree, counter_byref=counter_byref, verbose=verbose,listsNodeSymbol=listsNodeSymbol, compact_single_dict=compact_single_dict)
    else:
        # if o is not a dict or list, then it is a node
        create_node(tree, str(o), counter_byref, verbose, parent_id=parent_id)
    return tree


def delete_node(tree, node_id):
    tree.remove_node(node_id)
    for child in tree.children(node_id):
        delete_node(tree, child.identifier)


def get_ancestors_by_keyword(tree, keyword):
    return [node.tag for node in tree.rsearch(keyword)]


# visualize tree and save to file .gv
def visualize_tree(tree):
    # visualize tree
    dot = Digraph(comment='code tree')
    # dot.attr('node', shape='box')
    for node in tree.all_nodes():
        dot.node(str(node.identifier), node.tag)
        if node.bpointer is not None:
            dot.edge(str(node.bpointer), str(node.identifier)) 
    dot.render('code_tree.gv', view=True)
    return dot



