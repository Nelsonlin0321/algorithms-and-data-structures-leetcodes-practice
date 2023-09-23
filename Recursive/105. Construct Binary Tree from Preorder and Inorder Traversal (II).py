from typing import List, Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base case
        if not inorder:
            return None

        # get the root val
        root_val = preorder.pop(0)
        root = TreeNode(val=root_val)
        root_index = inorder.index(root_val)
        root.left = self.buildTree(preorder, inorder=inorder[:root_index])
        root.right = self.buildTree(preorder, inorder=inorder[root_index+1:])

        return root
