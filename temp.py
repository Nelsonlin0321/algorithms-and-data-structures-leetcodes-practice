from typing import List

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getNthFromEnd(head: ListNode, n: int) -> ListNode:
    fast = head
    for _ in range(n):
        fast = fast.next

    slow = head
    while fast:
        fast = fast.next
        slow = slow.next

    return slow


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodeBeforeN = getNthFromEnd(head, n+1)
        nodeBeforeN.next = nodeBeforeN.next.next
        return head


def convertArrayToLinkedList(nums: List[int]) -> ListNode:
    if not nums:
        return None
    head = ListNode(val=nums[0])
    head.next = convertArrayToLinkedList(nums=nums[1:])
    return head


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    head = convertArrayToLinkedList(nums)
    node = getNthFromEnd(head, 3)
    print(node.val)
    # while head:
    #     print(head.val)
    #     head = head.next
