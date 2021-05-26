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
            root.left = None
        return root


class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = [[root.val]]
        queue = [root]

        while len(queue) != 0:

            val_list = []

            size = len(queue)

            for i in range(size):

                node = queue[i]

                if node.left is not None:
                    queue.append(node.left)
                    val_list.append(node.left.val)

                if node.right is not None:
                    queue.append(node.right)
                    val_list.append(node.right.val)

            queue = queue[size:]

            if len(val_list) != 0:
                res.append(val_list)
        return res


if __name__ == "__main__":
    root = [3, 9, 20, None, None, 15, 7]
    binary_tree = BinaryTree()
    root = binary_tree(root)

    res = Solution().levelOrder(root)
    print(res)
# array_nums = [1, 2, 3, 4, 5, 6, 7]
#
# print("Original array:")
# print(array_nums)
# result = array_to_bst(array_nums)
# print("\nArray to a height balanced BST:")
# print(preOrder(result))
