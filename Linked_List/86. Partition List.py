# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import Optional

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        p = head
        left_nodes = ListNode(-1)
        left_p = left_nodes
        right_nodes = ListNode(-1)
        right_p = right_nodes
        
        while p:
            if p.val < x:
                left_p.next = p
                left_p = left_p.next
            else:
                right_p.next = p
                right_p = right_p.next
            
            # hard to understand
            # 断开原链表中的每个节点的 next 指针
            # p = p.next
            temp = p.next # 先保留下一个节点
            p.next = None # 当前的 p 的下一个节点设置为空
            p = temp
        
        left_p.next = right_nodes.next
        
        return left_nodes.next
                 
        