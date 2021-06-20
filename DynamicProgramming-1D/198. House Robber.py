from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        # base case
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        dp = [0 for _ in range(len(nums))]
        # base case
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for t in range(2, len(nums)):
            dp[t] = max(dp[t - 2] + nums[t], dp[t - 1])

        return dp[-1]

if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(Solution().rob(nums))
