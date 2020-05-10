# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

"""
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""

# Node Structure 
class Node:
    # Utility function to create a new node 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# function increments count by number of single valued subtrees under root
# returns true is subtree under root is singly, else false
def countSingleRec(root, count):
    
    # return true to indicate none
    if root is None:
        return True
    
    # recursively count in left and right subtrees
    left = countSingleRec(root.left, count)
    right = countSingleRec(root.right, count)

    # if any of the subtrees is not singly, then return false
    if left == False or right == False:
        return False

    # if left subtree is singly and non-empty but data doesnt match
    if root.left and root.data != root.left.data:
        return False

    # if right subtree is singly and non-empty but data doesnt match
    if root.right and root.data != root.right.data:
        return False
    
    # if none of the above conditions is True then tree rooted under root is single valued
    # increment count and return True
    count[0] += 1
    return True


def countSingle(root):
    # initialise result
    count = [0]

    # recursive function to count
    countSingleRec(root, count)

    return count[0]

# Driver program to test  
  

# Let us construct the below tree  
#       5 
#     /   \ 
#    4      5 
#  /  \      \ 
# 4    4      5 


root = Node(5)
root.left = Node(4) 
root.right = Node(5) 
root.left.left = Node(4) 
root.left.right = Node(4) 
root.right.right = Node(5)


print(countSingle(root))
