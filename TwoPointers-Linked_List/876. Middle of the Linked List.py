# Definition for singly-linked list.
# Runtime: 32 ms, faster than 45.53% of Python3 online submissions for Middle of the Linked List.
# Memory Usage: 14.3 MB, less than 8.31% of Python3 online submissions for Middle of the Linked List.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def middleNode(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next

        if fast.next is not None:
            return slow.next

        return slow


if __name__ == "__main__":
    pass
