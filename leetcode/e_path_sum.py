# given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum


def hasPathSum(root, sum):

    def helper(node, target):

        if not node:
            return False

        target -= node.val

        if (target == 0) and (not node.left) and (not node.right):
            return True

        return helper(node.left, target) or helper(node.right, target)

    if not root:
        return

    return helper(root, sum)