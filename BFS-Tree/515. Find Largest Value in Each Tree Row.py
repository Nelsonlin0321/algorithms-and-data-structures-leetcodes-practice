# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        max_nums = []
        # base case
        if not root:
            return max_nums

        q = [root]
        while q:
            size = len(q)
            layer_max = -float("inf")
            for i in range(size):
                node = q[i]
                layer_max = max(layer_max, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            max_nums.append(layer_max)
            q = q[size:]

        return max_nums
