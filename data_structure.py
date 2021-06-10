from typing import List, Optional


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
        # print(root.val)
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


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __call__(self, array):
        return self.arrayToList(array)

    def arrayToList(self, nums: List[int]) -> Optional[ListNode]:
        return self.convert(nums)

    def convert(self, nums):
        if len(nums) == 0:
            return None
        root_node = ListNode(val=nums[0])
        root_node.next = self.convert(nums[1:])
        return root_node


if __name__ == "__main__":
    # head = [1, 2, 3, 4, 5]
    # linked_list = LinkedList()
    # linked_list = linked_list(head)
    #
    # while linked_list is not None:
    #     print(linked_list.val)
    #     linked_list = linked_list.next
    null = None
    head = [3, 9, 20, null, null, 15, 7]
    binary_tree = BinaryTree()
    binary_tree = binary_tree(head)
