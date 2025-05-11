# Definition for singly-linked list.
from typing import List, Optional
import heapq
"""
Accepted
134 / 134 testcases passed
Nelson Lin
Nelson Lin
submitted at May 11, 2025 23:40
Runtime
15ms
Beats38.90%
Analyze Complexity
Memory
20.36MB
Beats36.44%
Analyze Complexity
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        pq = []
        dummy = ListNode(val=None)

        for index, head in enumerate(lists):
            if head:
                heapq.heappush(pq, (head.val, index, head))

        curr_node = dummy
        while pq:
            val, index, node = heapq.heappop(pq)
            curr_node.next = node
            curr_node = node
            if node.next:
                heapq.heappush(pq, (node.next.val, index, node.next))

        return dummy.next


if __name__ == "__main__":
    lists = [[1, 4, 5],
             [1, 3, 4],
             [2, 6]]

    lists = [(convert_list_to_linkedList(l)) for l in lists]

    mergedList = Solution().mergeKLists(lists)
    # print_linkedList(lists[3])
