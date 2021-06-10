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


if __name__ == "__main__":
    null = None
    array = [0, -3, 9, -10, null, 5]
    binary_tree = BinaryTree()
    root = binary_tree(array)
    print(root)
