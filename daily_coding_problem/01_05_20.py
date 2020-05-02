# Given the root to a binary tree:
# implement serialize(root), which serializes the tree into a string
# and deserialize(s), which deserializes the string back into the tree

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    
    if not root:
        return None

    

node_a = Node('a')

print(node_a.val)