from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Runtime
Details
44ms
Beats 94.10%of users with Python3
Memory
Details
20.41MB
Beats 47.87%of users with Python3
"""


class Solution:

    def __init__(self) -> None:
        self.rank = 0
        self.res = None

    def inorder_traverse(self, root: Optional[TreeNode], k):
        if root is None:
            return
        self.inorder_traverse(root.left, k)
        self.rank += 1
        if self.rank == k:
            self.res = root.val
            return
        self.inorder_traverse(root.right, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.inorder_traverse(root, k)

        return self.res
