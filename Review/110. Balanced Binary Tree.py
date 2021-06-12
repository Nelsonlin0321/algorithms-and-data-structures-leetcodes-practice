from utils import random_question

# print(random_question())
# 110. Balanced Binary Tree.py
# https://leetcode.com/problems/balanced-binary-tree/

"""
110. Balanced Binary Tree
Easy

3674

237

Add to List

Share
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
"""

from data_structure import BinaryTree, TreeNode


class Solution:
    """
    # Runtime: 68 ms, faster than 24.26% of Python3 online submissions for Balanced Binary Tree.
    # Memory Usage: 18 MB, less than 88.78% of Python3 online submissions for Balanced Binary Tree.

    """

    def get_height(self, root):
        if root is None:
            return 0

        return 1 + max(self.get_height(root.left),
                       self.get_height(root.right))

    def isBalanced(self, root: TreeNode) -> bool:

        # conquer the smallest problem
        if root is None:
            return True

        # divide
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)

        if abs(left_height - right_height) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)


class Solution:

    """
    Runtime: 52 ms, faster than 66.15% of Python3 online submissions for Balanced Binary Tree.
    Memory Usage: 18.2 MB, less than 63.37% of Python3 online submissions for Balanced Binary Tree.
    """

    def __init__(self):
        self.is_balanced = True

    def get_height(self, root):
        # the conquer, the smallest problem
        if root is None:
            return 0

        # divide the problem to subproblm

        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)

        if abs(left_height - right_height) > 1:
            self.is_balanced = False

        return 1 + max(left_height, right_height)

    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True

        _ = self.get_height(root)
        return self.is_balanced


if __name__ == "__main__":
    null = None
    root = [3, 9, 20, null, null, 15, 7]
    binary_tree = BinaryTree()
    root = binary_tree(root)

    print(Solution().isBalanced(root))
