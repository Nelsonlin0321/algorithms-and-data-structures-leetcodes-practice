# https://leetcode.com/problems/sort-colors/


# Bubble Sort Solution
"""
Runtime: 69 ms, faster than 14.39% of Python3 online submissions for Sort Colors.
Memory Usage: 13.9 MB, less than 63.78% of Python3 online submissions for Sort Colors.

"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [!Important] move the i largest to i th position, from the largest to the smallest
        for i in range(len(nums) - 1, 0, -1):
            for j in range(i):
                left = nums[j]
                right = nums[j + 1]

                if left > right:
                    nums[j + 1] = left
                    nums[j] = right
"""
Accepted
89 / 89 testcases passed
Nelson Lin
Nelson Lin
submitted at May 17, 2025 13:07
Runtime
0ms
Beats100.00%
Analyze Complexity
Memory
17.83MB
Beats33.54%
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums)-1
        p = 0 

        while p <= right:

            if nums[p] == 0:
                nums[p],nums[left] =nums[left],nums[p]
                left+=1

            elif nums[p] == 2:
                nums[p],nums[right] =nums[right],nums[p]
                right-=1

            elif nums[p]==1:
                p+=1

            if left>p:
                p=left
        

var_list = [2, 3, 4, 5, 321, 1]
solution = Solution()
solution.sortColors(var_list)
print(var_list)
