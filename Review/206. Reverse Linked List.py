from typing import Optional

from data_structure import ListNode

"""
Runtime: 32 ms, faster than 86.89% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.6 MB, less than 45.33% of Python3 online submissions for Reverse Linked List.
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if head is None:
            return None

        prev = None
        curr = head

        while (curr is not None):
            # 1) get the next node first
            next = curr.next

            # 2) reverse the curr link
            curr.next = prev

            # 3) move forwards
            prev = curr
            curr = next
        return prev







