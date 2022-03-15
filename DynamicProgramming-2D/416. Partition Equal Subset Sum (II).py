"""
Success
Details
Runtime: 4233 ms, faster than 12.83% of Python3 online submissions for Partition Equal Subset Sum.
Memory Usage: 29.9 MB, less than 33.83% of Python3 online submissions for Partition Equal Subset Sum.
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_ % 2 == 1:
            return False

        target = sum_ // 2 #

        row = [False for _ in range(target + 1)]
        dp = [row.copy() for _ in range(len(nums) + 1)]

        # dp[i][target] definition: 对于前i 个物品，包括i 时候可以选择 组成 target

        # base case
        for i in range(len(nums) + 1):
            dp[i][0] = True

        for w in range(target + 1):
            dp[0][w] = False

        for i in range(1, len(nums) + 1):
            for w in range(1, target + 1):
                if nums[i - 1] > w:
                    dp[i][w] = dp[i - 1][w]
                else:
                    dp[i][w] = dp[i - 1][w - nums[i - 1]] or dp[i - 1][w]

        return dp[-1][-1]
