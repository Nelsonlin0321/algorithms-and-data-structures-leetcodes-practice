# https://leetcode.com/problems/sort-colors/


# Bubble Sort Solution
"""
Runtime: 69 ms, faster than 14.39% of Python3 online submissions for Sort Colors.
Memory Usage: 13.9 MB, less than 63.78% of Python3 online submissions for Sort Colors.

"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #[!Importantt] move the i largest to i th position, from the largest to the smallest
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i):
                left = nums[j]
                right = nums[j + 1]

                if left > right:
                    nums[j + 1] = left
                    nums[j] = right


