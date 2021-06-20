from typing import List


class Solution:
    """
    Runtime: 2824 ms, faster than 29.44% of Python3 online submissions for Partition Equal Subset Sum.
    Memory Usage: 30.3 MB, less than 40.40% of Python3 online submissions for Partition Equal Subset Sum.
    """
    def canPartition(self, nums: List[int]) -> bool:

        # base case
        if len(nums) <= 1:
            return False

        target_sum = sum(nums)
        target_sum = target_sum / 2

        if target_sum > int(target_sum):
            return False
        else:
            target_sum = int(target_sum)

        N = [None for _ in range(len(nums) + 1)]
        dp = [N.copy() for _ in range(target_sum + 1)]

        # base case
        # dp[target_sum][N (item)]

        # sum = 0
        for n in range(len(nums) + 1):
            dp[0][n] = True  # 当背包没有空间时，相当于装满了

        # N item = 0
        for m in range(target_sum + 1):
            dp[m][0] = False

        # print(len(dp))
        # print(len(dp[0]))
        for n in range(1, len(nums) + 1):
            for m in range(1, target_sum + 1):
                n_val = nums[n - 1]
                if n_val > m:
                    dp[m][n] = dp[m][n - 1]
                else:
                    dp[m][n] = dp[m][n - 1] or dp[m - n_val][n - 1]
        return dp[-1][-1]


class Solution:
    """
    Runtime: 4160 ms, faster than 9.39% of Python3 online submissions for Partition Equal Subset Sum.
    Memory Usage: 30.6 MB, less than 22.17% of Python3 online submissions for Partition Equal Subset Sum.
    """
    def __init__(self):
        self.dp = None

    def canPartition(self, nums: List[int]) -> bool:

        # base case
        if len(nums) <= 1:
            return False

        target_sum = sum(nums)
        target_sum = target_sum / 2

        if target_sum > int(target_sum):
            return False
        else:
            target_sum = int(target_sum)

        N = [None for _ in range(len(nums) + 1)]
        dp = [N.copy() for _ in range(target_sum + 1)]

        # base case
        # dp[target_sum][N (item)]
        # sum = 0
        for n in range(len(nums) + 1):
            dp[0][n] = True  # 当背包没有空间时，相当于装满了

        # N item = 0
        for m in range(target_sum + 1):
            dp[m][0] = False

        m = target_sum
        n = len(nums)
        return self.partition(m, n, nums, dp)

    def partition(self, m, n, nums, dp):

        n_val = nums[n - 1]

        if n_val > m:
            if dp[m][n - 1] is None:
                dp[m][n - 1] = self.partition(m, n - 1, nums, dp)
                return dp[m][n - 1]
            else:
                return dp[m][n - 1]

        else:
            if dp[m][n - 1] is None:
                dp[m][n - 1] = self.partition(m, n - 1, nums, dp)

            if dp[m - n_val][n - 1] is None:
                dp[m - n_val][n - 1] = self.partition(m - n_val, n - 1, nums, dp)

            dp[m][n] = dp[m][n - 1] or dp[m - n_val][n - 1]

            return dp[m][n]


nums = [1, 5, 11, 5]
print(Solution().canPartition(nums))
