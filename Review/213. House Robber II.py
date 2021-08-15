from typing import List


class Solution:
    """
    Runtime: 24 ms, faster than 96.41% of Python3 online submissions for House Robber II.
    Memory Usage: 14.4 MB, less than 5.71% of Python3 online submissions for House Robber II.
    """
    def rob(self, nums: List[int]) -> int:
        # base case

        if len(nums) <= 2:
            return max(nums)

        head = nums[:-1]
        tail = nums[1:]

        head_max = self.helper(head)
        tail_max = self.helper(tail)

        return max(head_max, tail_max)

    def helper(self, nums: List[int]):
        # base case
        if len(nums) == 0:
            return 0
        elif len(nums) <= 2:
            return max(nums)

        dp = [None for _ in range(len(nums))]
        # smallest problem

        dp[0] = nums[0]
        dp[1] = max(nums[:2])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]


if __name__ == "__main__":
    nums = [1]
    # print(Solution().helper(nums))
    print(Solution().rob(nums))
    # print(nums[:-1])
