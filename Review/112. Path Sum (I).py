from data_structure import TreeNode, BinaryTree


class Solution:
    """
    Runtime: 40 ms, faster than 84.50% of Python3 online submissions for Path Sum.
    Memory Usage: 16.1 MB, less than 23.12% of Python3 online submissions for Path Sum.
    """
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # the smallest problem
        # conquer
        if root is None:
            return False
        if root.val == targetSum and (root.left is None and root.right is None):
            return True

        # divide / combine
        left_has_sum = self.hasPathSum(root.left, targetSum - root.val)
        if left_has_sum:
            return True

        right_has_sum = self.hasPathSum(root.right, targetSum - root.val)

        if right_has_sum:
            return True

        return False


if __name__ == "__main__":
    null = None
    root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1]
    root = BinaryTree().arrayToBST(root)

    targetSum = 22
    print(Solution().hasPathSum(root, targetSum))
