# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/submissions/
# Runtime: 64 ms, faster than 28.44% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
# Memory Usage: 15.7 MB, less than 58.82% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.convert(nums)

    def convert(self, nums):
        if len(nums) == 0:
            return None

        mid = len(nums) // 2

        root = TreeNode(val=nums[mid])
        root.left = self.convert(nums[:mid])

        root.right = self.convert(nums[mid + 1:])

        return root
