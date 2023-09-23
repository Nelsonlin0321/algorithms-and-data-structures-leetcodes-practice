from typing import Optional, List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Runtime
Details
36ms
Beats 74.48%of users with Python3
Memory
Details
16.27MB
Beats 66.05%of users with Python3
"""


class Solution:
    def __init__(self) -> None:
        self.res = []

    def traverse(self, root: Optional[TreeNode]) -> None:
        # base case
        if root is None:
            return
        self.traverse(root.left)
        self.res.append(root.val)
        self.traverse(root.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        self.traverse(root)
        return self.res
