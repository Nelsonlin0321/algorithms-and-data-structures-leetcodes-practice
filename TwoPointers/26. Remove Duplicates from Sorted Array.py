# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
Success
Details 
Runtime: 86 ms, faster than 97.36% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.5 MB, less than 96.47% of Python3 online submissions for Remove Duplicates from Sorted Array.
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # base case
        if len(nums)<=1:
            return len(nums)
        
        slow = 0
        fast = 0
        
        while fast <= len(nums)-1:
            
            if nums[slow] == nums[fast]:
                fast+=1
            elif  nums[slow] != nums[fast]:
                slow+=1
                nums[slow] = nums[fast]
                fast+=1        
        
        return slow+1
        

if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(Solution().removeDuplicates(nums))
    
            
        
        
        
        
        