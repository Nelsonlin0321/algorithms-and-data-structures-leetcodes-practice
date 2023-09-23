from typing import Optional


"""
Runtime
Details
79ms
Beats 58.66%of users with Python3
Memory
Details
23.65MB
Beats 97.07%of users with Python3
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self) -> None:
        self.res = -float("inf")

    def oneSideSum(self, root: Optional[TreeNode]):

        # base case
        if root is None:
            return 0

        # post ordering
        left_path_sum = max(0, self.oneSideSum(root.left))
        right_path_sum = max(0, self.oneSideSum(root.right))

        current_node_path = root.val + left_path_sum + right_path_sum
        self.res = max(current_node_path, self.res)

        # the function to return one of left or right path
        return root.val + max(left_path_sum, right_path_sum)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.oneSideSum(root)
        return self.res
