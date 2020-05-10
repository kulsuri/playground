# Given the root to a binary tree:
# implement serialize(root), which serializes the tree into a string
# and deserialize(s), which deserializes the string back into the tree

import json
import pprint

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    
    if not root:
        return None

    serialized_tree_map = dict()
    serialized_left = serialize(root.left)
    serialized_right = serialize(root.right)

    serialized_tree_map['data'] = root.val

    if serialized_left:
        serialized_tree_map['left'] = serialized_left
    if serialized_right:
        serialized_tree_map['right'] = serialized_right
    
    return json.dumps(serialized_tree_map)

def deserialize(serialized_tree_map_json):
    
    serialized_tree_map_json = json.loads(serialized_tree_map_json)

    node = Node(serialized_tree_map_json['data'])

    if 'left' in serialized_tree_map_json:
        node.left = deserialize(serialized_tree_map_json['left'])
    if 'right' in serialized_tree_map_json:
        node.right = deserialize(serialized_tree_map_json['right'])

    return node

# initialize nodes
node_a = Node('a')
node_b = Node('b')
node_c = Node('c')
node_d = Node('d')
node_e = Node('e')
node_f = Node('f')
node_g = Node('g')

# initialize tree
node_a.left = node_b
node_a.right = node_c
node_b.left = node_d
node_b.right = node_e
node_c.left = node_f
node_c.right = node_g

"""
     a
   /  \
  b    c
 /\    /\
d  e  f  g
""" 

serialized_a = serialize(node_a)
pprint.pprint(json.loads(serialized_a))

deserialized_a = deserialize(serialized_a)

print(deserialized_a.val) # prints a
print(deserialized_a.left.val) # prints b
print(deserialized_a.right.val) # prints c
print(deserialized_a.left.left.val) # prints d
print(deserialized_a.left.right.val) # prints e

assert deserialized_a.val == "a"
assert deserialize( serialize(node_a) ).left.left.val == 'd'