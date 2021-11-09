# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
from typing import Optional
from data_structure import TreeNode, BinaryTree


### 题目没有理解对！每一个子树都要balance
class Solution:
    def getHeight(self, root):
        # base case
        if root is None:
            return 0

        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)

        return 1 + max(left_height, right_height)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # base case
        if root is None:
            return True
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)

        if abs(left_height - right_height) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)


# better solution
"""
Runtime: 52 ms, faster than 74.36% of Python3 online submissions for Balanced Binary Tree.
Memory Usage: 18 MB, less than 75.40% of Python3 online submissions for Balanced Binary Tree.
"""
class Solution:

    def __init__(self):
        self.is_balanced = True

    def getHeight(self, root):
        # base case
        # conqure
        if root is None:
            return 0
        # divide
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)

        if abs(left_height - right_height) > 1:
            self.is_balanced = False
        # combine
        return 1 + max(left_height, right_height)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        _ = self.getHeight(root)
        return self.is_balanced


if __name__ == "__main__":
    null = None
    root = [3, 9, 20, null, null, 15, 7]
    root = BinaryTree.arrayToBST(root)
    print(Solution().isBalanced(root))
