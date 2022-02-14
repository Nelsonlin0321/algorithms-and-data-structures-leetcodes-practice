# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head
        fast = head
        if next is None:
            return False

        while slow is not None or fast.next is not None:
            slow = slow.next
            fast = slow.next.next
            if slow == fast:
                return True

        return False
