from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def convert_array_binary_tree(nums: List[int]):
    def convert(nums, root_idx):

        val = nums[root_idx]

        if val is None:
            return None

        root = TreeNode(val)
        left_idx = root_idx * 2 + 1
        right_idx = left_idx + 1

        if left_idx <= len(nums) - 1:
            root.left = convert(nums, left_idx)
        if right_idx <= len(nums) - 1:
            root.right = convert(nums, right_idx)

        return root

    return convert(nums, 0)


null = None
nodes = [3, 9, 20, null, null, 15, 7]

root = convert_array_binary_tree(nodes)


def preOderTraverse(root):
    if root is not None:
        print(root.val, " ")
        preOderTraverse(root.left)
        preOderTraverse(root.right)


def inOderTraverse(root):
    if root is not None:
        inOderTraverse(root.left)
        print(root.val, " ")
        inOderTraverse(root.right)


def postOderTraverse(root):
    if root is not None:
        postOderTraverse(root.left)
        postOderTraverse(root.right)
        print(root.val, " ")


if __name__ == "__main__":
    # preOderTraverse(root)
    # inOderTraverse(root)
    postOderTraverse(root)
