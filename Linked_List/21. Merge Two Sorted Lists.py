# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = ListNode(-1)
        
        # the pointer to change the linked list
        pointer = mergedList
        
        while list1  and list2:
            if list1.val <= list2.val:
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next
            
            pointer = pointer.next
                
        if list1:
            pointer.next = list1
            
        if list2:
            pointer.next = list2
        
        return mergedList.next
                
             
        
        