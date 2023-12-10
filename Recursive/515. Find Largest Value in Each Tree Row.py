# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):

        self.max_nums = {}

    def traverse(self, root, depth):
        if not root:
            return
        if depth not in self.max_nums:
            self.max_nums[depth] = root.val
        else:
            self.max_nums[depth] = max(root.val, self.max_nums[depth])
        self.traverse(root.left, depth+1)
        self.traverse(root.right, depth+1)

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse(root, 0)
        print(self.max_nums)
        return list(self.max_nums.values())
