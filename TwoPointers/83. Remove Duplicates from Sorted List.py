
from typing import Optional, List

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def convert(nums):
    if len(nums) == 0:
        return None
    root_node = ListNode(val=nums[0])
    root_node.next = convert(nums[1:])
    return root_node


def print_linked_list(nodes):
    while nodes is not None:
        print(nodes.val)
        nodes = nodes.next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if head is None:
            return head

        slow = head
        fast = head.next

        while fast:
            if fast.val == slow.val:
                # the slow remains unchanged
                fast = fast.next
            elif fast.val != slow.val:
                # the slow and fast move together
                # assign the fast next value to slow
                slow.next = fast
                fast = fast.next
                slow = slow.next

        slow.next = None

        return head


if __name__ == "__main__":
    head = [1, 1, 2]
    head = convert(head)
    # print(head)
    # print_linked_list(head)
    res = Solution().deleteDuplicates(head)
    print_linked_list(res)
