# https://leetcode.com/problems/minimum-depth-of-binary-tree/
from typing import Optional

from data_structure import TreeNode

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
            # breath function
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
            queue = queue[size:]  # reduce
