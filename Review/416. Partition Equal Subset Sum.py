from typing import List


class Solution:

    def __init__(self):
        self.dp = None

    def canPartition(self, nums: List[int]) -> bool:
        sum_val = sum(nums)

        if sum_val % 2 != 0:
            return False

        """create dp : dp[N][M], N is the number of item, M is the size of packet"""
        target_sum = sum_val // 2
        M = [None for _ in range(target_sum + 1)]
        dp = [M.copy() for _ in range(len(nums) + 1)]

        """base cases 1: dp[N][M], N =0 which means no item. All False"""
        for M in range(target_sum + 1):
            dp[0][M] = False

        """base cases 2: dp[N][M], M =0 which means it's already full. All True"""
        for N in range(len(nums) + 1):
            dp[N][0] = True

        """ loop the sub-problem: status"""

        for M in range(1, target_sum + 1):
            for N in range(1, len(nums) + 1):

                item_val = nums[N - 1]

                """the item is larger than the size of pocket, cannot install it"""
                if item_val > M:
                    dp[N][M] = dp[N - 1][M]
                else:
                    """selection: install it or not"""
                    dp[N][M] = dp[N - 1][M] or dp[N - 1][M - item_val]
        return dp[-1][-1]


if __name__ == "__main__":
    nums = [1, 2, 3, 5]
    print(Solution().canPartition(nums))
