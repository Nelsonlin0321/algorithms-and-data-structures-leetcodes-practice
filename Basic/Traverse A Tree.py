# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traverse(root: TreeNode):
    # executing current node is pre_ordering
    # the current node is always high priority
    print(root.val)
    preorder_traverse(root.left)
    preorder_traverse(root.right)


def inorder_traverse(root: TreeNode):
    # executing left node is  in_ordering
    # the left node is always high priority
    inorder_traverse(root.left)
    print(root.val)
    preorder_traverse(root.right)


def postorder_traverse(root: TreeNode):
    # executing right node is  in_ordering
    # the left node is always high priority

    preorder_traverse(root.left)
    preorder_traverse(root.right)
    print(root.val)
