# https://leetcode.com/problems/minimum-depth-of-binary-tree/
from typing import Optional

from data_structure import TreeNode


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

### ? why
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # base case
        if root is None:
            return 0

        # init queque
        queque = [root]
        depth = 1
        while (len(queque) != 0):
            next_quque = []

            for node in queque:

                _ = queque.pop(0)

                left = node.left
                right = node.right

                if left is None and right is None:
                    return depth

                if left is not None:
                    next_quque.append(left)

                if right is not None:
                    next_quque.append(right)

            depth += 1
            queque.extend(next_quque)

"""
Runtime: 468 ms, faster than 94.47% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 49 MB, less than 85.75% of Python3 online submissions for Minimum Depth of Binary Tree.
"""

class Solution:

    def minDepth(self, root: TreeNode) -> int:
        deepth = 0
        # base case
        if root is None:
            return deepth

        deepth = 1
        # init
        queue = [root]

        while len(queue) != 0:

            size = len(queue)
            # breatch function
            # important technique #  remember
            for idx in range(size):

                node = queue[idx]

                left = node.left
                right = node.right

                if left is None and right is None:
                    return deepth

                if left is not None:
                    queue.append(left)

                if right is not None:
                    queue.append(right)

            deepth += 1
            queue = queue[size:] # reduce


