"""
Success
Details
Runtime: 44 ms, faster than 85.59% of Python3 online submissions for Path Sum.
Memory Usage: 15.2 MB, less than 35.38% of Python3 online submissions for Path Sum.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        # base case

        # conqur to solve the small problem
        if root is None:
            return False

        if root.left is None and root.right is None and root.val == targetSum:
            return True

        # divid the problem to be sub problem
        if root.left is not None:
            leftHasPathSum = self.hasPathSum(root.left, targetSum - root.val)
            if leftHasPathSum:
                return True

        if root.right is not None:
            RightHasPathSum = self.hasPathSum(root.right, targetSum - root.val)
            if RightHasPathSum:
                return True
        # combine
        return False


