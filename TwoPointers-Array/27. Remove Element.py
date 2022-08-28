# https://leetcode.com/problems/remove-element/

"""
Success
Details 
Runtime: 41 ms, faster than 80.37% of Python3 online submissions for Remove Element.
Memory Usage: 13.9 MB, less than 14.44% of Python3 online submissions for Remove Element.
"""

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums)==0:
            return 0
        
        
        slow = 0
        fast = 0
        
        while fast < len(nums)-1:
            if nums[fast] != val:
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
            
        return slow
            
    