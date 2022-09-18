# https://leetcode.com/problems/add-two-numbers/

"""
Success
Details 
Runtime: 85 ms, faster than 78.09% of Python3 online submissions for Add Two Numbers.
Memory Usage: 13.9 MB, less than 43.24% of Python3 online submissions for Add Two Numbers.
"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head_l1 = l1
        nums_l1 = []
        while head_l1:
            nums_l1.append(head_l1.val)
            head_l1 = head_l1.next

        nums_l1 = [10**i * num for (i, num) in enumerate(nums_l1)]
        num_l1 = sum(nums_l1)

        head_l2 = l2
        nums_l2 = []
        while head_l2:
            nums_l2.append(head_l2.val)
            head_l2 = head_l2.next

        nums_l2 = [10**i * num for (i, num) in enumerate(nums_l2)]
        num_l2 = sum(nums_l2)

        add_nums = list(str(num_l1+num_l2))
        add_nums = [int(num) for num in add_nums]

        tail_head = ListNode(add_nums[0], None)
        add_nums = add_nums[1:]

        while add_nums:
            val = add_nums.pop(0)
            tail_head = ListNode(val, tail_head)

        return tail_head