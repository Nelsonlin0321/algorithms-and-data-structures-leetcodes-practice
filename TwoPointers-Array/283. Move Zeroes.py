# https://leetcode.com/problems/move-zeroes/
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0 # the pointer, the left of which are non-zeros
        fast = 0
        
        while fast < len(nums):
            if nums[fast] != 0:
                # the non-zero val moved ahead
                nums[fast],nums[slow] =nums[slow], nums[fast]
                slow+=1
            fast+=1
            
            
if __name__ == "__main__":
    nums = [0,1,0,3,12]
    Solution().moveZeroes(nums)
    print(nums)
    
     
                
                
            
            
            
        
        
        