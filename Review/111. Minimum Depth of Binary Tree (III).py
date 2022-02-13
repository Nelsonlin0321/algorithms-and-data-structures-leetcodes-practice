# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



"""
Runtime: 532 ms, faster than 86.10% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 49.4 MB, less than 65.06% of Python3 online submissions for Minimum Depth of Binary Tree.
"""

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        # base case

        if root is None:
            return 0

        depth = 1
        queque = [root]

        while len(queque) != 0:
            print(depth)
            size = len(queque)
            # first layer loop for root
            for index in range(size):
                curr_node = queque[index]
                if curr_node.left is None and curr_node.right is None: # 搜索到达的目标
                    return depth

                # second layer loop for curr_node:
                # 有条件的把邻居加入
                left_node = curr_node.left
                if left_node is not None:
                    queque.append(left_node)
                right_node = curr_node.right
                if right_node is not None:
                    queque.append(right_node)

            queque = queque[size:]
            depth += 1

        return depth
