# Definition for singly-linked list.
from typing import Optional
"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/submissions/1631074586/ 
Accepted
166 / 166 testcases passed
Nelson Lin
Nelson Lin
submitted at May 11, 2025 21:43
Runtime
0ms
Beats100.00%
Analyze Complexity
Memory
17.78MB
Beats70.73%

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def convert_list_to_linkedList(arr):
    tail = None
    head = None
    for i in range(len(arr)-1, -1, -1):
        head = ListNode(val=arr[i])
        head.next = tail
        tail = head
    return head


def print_linkedList(head: ListNode):

    while head:
        print(head.val)
        head = head.next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(val=None)
        dummyNode.next = head

        left = dummyNode
        right = left.next

        detect_same = False

        while (right is not None) and (right.next is not None):

            if left.next.val != right.next.val:

                if not detect_same:
                    left = left.next
                    right = right.next

                if detect_same:
                    # detect same but nodes are different, need to remove
                    left.next = right.next
                    detect_same = False
                    right = left.next
            else:
                right = right.next
                detect_same = True

        if detect_same:
            # remove the rest of same node
            left.next = None

        return dummyNode.next


if __name__ == "__main__":
    arr = [1, 1, 2, 3, 6, 6]
    head = convert_list_to_linkedList(arr)
    result_node = Solution().deleteDuplicates(head)
    print_linkedList(result_node)
