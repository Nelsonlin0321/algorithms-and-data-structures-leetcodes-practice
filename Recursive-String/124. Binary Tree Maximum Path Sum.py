# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from data_structure import TreeNode


class Solution:

    def __init__(self):
        self.res = -float("inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        _ = self.getMaxPathSum(root)
        return self.res

    def getMaxPathSum(self, root: Optional[TreeNode]) -> int:
        # base case
        if root is None:
            return 0

        cur_val = root.val
        left_max = max(0, self.maxPathSum(root.left))
        right_max = max(0, self.maxPathSum(root.right))

        self.res = max(self.res, left_max + right_max + cur_val)
        return max(left_max, right_max) + cur_val
