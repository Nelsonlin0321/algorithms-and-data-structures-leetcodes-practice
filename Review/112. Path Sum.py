from utils import random_question

# print(random_question())  112. Path Sum.py
# https://leetcode.com/problems/path-sum/


from data_structure import TreeNode, BinaryTree


class Solution:
    """
    Runtime: 40 ms, faster than 82.29% of Python3 online submissions for Path Sum.
    Memory Usage: 16.1 MB, less than 9.80% of Python3 online submissions for Path Sum.
    """

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # base case
        if root is None:
            return False

        # conquer: 定义最小的问题，并且解决
        if root.left is None and root.right is None and root.val == targetSum:
            return True

        left_has_path_sum = False
        right_has_path_sum = False

        # divide： 拆分左右边
        if root.left is not None:
            left_has_path_sum = self.hasPathSum(root.left, targetSum - root.val)

        if root.right is not None:
            right_has_path_sum = self.hasPathSum(root.right, targetSum - root.val)

        # combine # 当任意一个是TRUE 的时候， 就返回True
        return left_has_path_sum or right_has_path_sum


if __name__ == "__main__":
    null = None
    root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1]
    root = BinaryTree()(root)
    targetSum = 22
    print(Solution().hasPathSum(root, targetSum))
