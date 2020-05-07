# Given the root to a binary tree:
# implement serialize(root), which serializes the tree into a string
# and deserialize(s), which deserializes the string back into the tree

import json

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    
    if not root:
        return None

    
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

print(node_a.val)