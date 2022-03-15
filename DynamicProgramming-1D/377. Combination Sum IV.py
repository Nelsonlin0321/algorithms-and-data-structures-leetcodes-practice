"""
Success
Details
Runtime: 36 ms, faster than 94.75% of Python3 online submissions for Combination Sum IV.
Memory Usage: 14 MB, less than 70.76% of Python3 online submissions for Combination Sum IV.
"""
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] = dp[i] + dp[i - num]

        return dp[-1]