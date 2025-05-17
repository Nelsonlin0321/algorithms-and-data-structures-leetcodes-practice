from typing import List
"""
Accepted
97 / 97 testcases passed
Nelson Lin
Nelson Lin
submitted at May 18, 2025 00:05
Runtime
131ms
Beats22.07%
Analyze Complexity
Memory
29.20MB
Beats37.51%
"""

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        target = total - x

        left = 0
        right = 0
        sum_ = 0
        min_oper = float("inf")
        while right<len(nums):
            sum_ +=nums[right]

            while sum_>target and left<=right:
                
                sum_-=nums[left]
                left+=1

            if sum_ == target:
                size = (right-left+1) 
                oper = len(nums) - size
                min_oper = min(oper,min_oper)
        
            right+=1

        return -1 if min_oper == float("inf") else min_oper
                    
        

        