from utils import random_question

# print(random_question())  # 111. Minimum Depth of Binary Tree.py

from data_structure import TreeNode, BinaryTree


class Solution:
    """
    Runtime: 592 ms, faster than 46.72% of Python3 online submissions for Minimum Depth of Binary Tree.
    Memory Usage: 53.1 MB, less than 37.22% of Python3 online submissions for Minimum Depth of Binary Tree.
    """

    def minDepth(self, root: TreeNode) -> int:

        # the base case
        if root is None:
            return 0

        # conquer the smallest problem
        if root.left is None and root.right is None:
            return 1

        # divide
        if root.left is not None and root.right is not None:
        # combine
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

        if root.left is not None:
            return 1 + self.minDepth(root.left)

        if root.right is not None:
            return 1 + self.minDepth(root.right)


null = None
root = [2, null, 3, null, 4, null, 5, null, 6]
root = BinaryTree()(root)

print(Solution().minDepth(root))
