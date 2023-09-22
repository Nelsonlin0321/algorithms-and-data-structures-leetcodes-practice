# Definition for a binary tree node.
from typing import List


# Runtime: 32 ms, faster than 99.22% of Python3 online submissions for Path Sum II.
# Memory Usage: 15.4 MB, less than 87.94% of Python3 online submissions for Path Sum II.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = []

    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if root is None:
            return self.res

        path = [root.val]

        self.backtrack(root, path, targetSum, root.val)

        return self.res

    def backtrack(self, root, path, targetSum, currSum):

        if root is None:
            return

        if root.left is None and root.right is None:
            if targetSum == currSum:
                self.res.append(path.copy())
                return
            else:
                return

        # loop the candidate
        if root.left is not None:
            path.append(root.left.val)
            # print(path)
            self.backtrack(root.left, path, targetSum, currSum + root.left.val)
            path.pop()

        if root.right is not None:
            path.append(root.right.val)
            self.backtrack(root.right, path, targetSum, currSum + root.right.val)
            path.pop()
