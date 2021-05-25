# Definition for a binary tree node.
# Runtime: 40 ms, faster than 71.60% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 16.2 MB, less than 35.18% of Python3 online submissions for Maximum Depth of Binary Tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
