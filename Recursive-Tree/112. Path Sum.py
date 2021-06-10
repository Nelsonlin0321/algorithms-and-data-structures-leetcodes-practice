from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def __call__(self, array):
        return self.arrayToBST(array)

    def arrayToBST(self, nums: List[int]) -> TreeNode:
        return self.convert(nums, 0)

    def convert(self, nums, root_idx):

        root = TreeNode(nums[root_idx])

        left_idx = root_idx * 2 + 1
        right_idx = left_idx + 1

        if left_idx <= len(nums) - 1 and nums[left_idx] is not None:
            root.left = self.convert(nums, left_idx)
        else:
            root.left = None

        if right_idx <= len(nums) - 1 and nums[right_idx] is not None:
            root.right = self.convert(nums, right_idx)
        else:
            root.right = None
        return root


class Solution:

    def hasPathSum(self, root, sum):
        # write code here
        if root is None:
            return False

        return self.backtracking(root, root.val, sum)

    def backtracking(self, root, cur_sum, target):
        if root.left is None and root.right is None:
            if cur_sum == target:
                return True
            else:
                return

        # left
        if root.left is not None:
            has_paths_sum = self.backtracking(root.left, cur_sum + root.left.val, target)
            if has_paths_sum:
                return True
        if root.right is not None:
            has_paths_sum = self.backtracking(root.right, cur_sum + root.right.val, target)
            if has_paths_sum:
                return True
        return False

# Runtime: 40 ms, faster than 81.74% of Python3 online submissions for Path Sum.
# Memory Usage: 16 MB, less than 30.44% of Python3 online submissions for Path Sum.

class Solution:

    def hasPathSum(self, root, sum):
        # write code here

        if root.left is None and root.right is None and sum-root.val ==0:
            return True

        if root.left is not None:
            left_has_path_sum = self.hasPathSum(root.left, sum - root.val)
            if left_has_path_sum:
                return True

        if root.right is not None:
            right_has_path_sum = self.hasPathSum(root.right,sum-root.val)
            if right_has_path_sum:
                return True
        return False



if __name__ == "__main__":
    null = None
    array = [1, 2]
    binary_tree = BinaryTree()
    root = binary_tree(array)
    print(Solution().hasPathSum(root, 3))
