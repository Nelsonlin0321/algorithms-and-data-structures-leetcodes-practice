from typing import Optional

from data_structure import TreeNode,array_to_binaryTree

class Solution:

    """
    Runtime: 36 ms, faster than 91.11% of Python3 online submissions for Maximum Depth of Binary Tree.
    Memory Usage: 15.9 MB, less than 73.87% of Python3 online submissions for Maximum Depth of Binary Tree.

    """

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # smalle problem
        if root is None:
            return 0

        # divide
        # combine

        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))




