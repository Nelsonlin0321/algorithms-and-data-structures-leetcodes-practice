from typing import List
"""
Success
Details 
Runtime: 4937 ms, faster than 29.83% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage: 14.2 MB, less than 85.98% of Python3 online submissions for Longest Increasing Subsequence.
"""

class Solution:

    def helper(self, i, nums, dp):
        max_length = 1
        # 在过去的数组中，寻找最小于当前值的最长子序列
        for j in range(i):
            if nums[i] > nums[j]:
                max_length = max(max_length, dp[j] + 1)

        return max_length

    def lengthOfLIS(self, nums: List[int]) -> int:
        # initiate
        max_length = 1
        dp = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            dp[i] = self.helper(i, nums, dp)
            max_length = max(max_length, dp[i])

        return max_length
