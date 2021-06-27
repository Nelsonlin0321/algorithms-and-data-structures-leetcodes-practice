from typing import List


class Solution:
    """
Runtime: 3768 ms, faster than 43.44% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage: 14.8 MB, less than 16.78% of Python3 online submissions for Longest Increasing Subsequence.
    """

    def lengthOfLIS(self, nums: List[int]) -> int:

        # base case I
        if not nums:
            return 0
        res = 1
        # base case II
        dp = [1 for _ in range(len(nums))]

        for idx in range(len(nums)):

            # find the number smaller than current num
            for jdx in range(idx):
                if nums[jdx] < nums[idx]:
                    dp[idx] = max(dp[jdx] + 1, dp[idx])

            res = max(res, dp[idx])

        return res


if __name__ == "__main__":
    nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]

    print(Solution().lengthOfLIS(nums))
