# https://leetcode.com/problems/longest-increasing-subsequence/
"""
300. Longest Increasing Subsequence
Medium

14691

265

Add to List

Share
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if not nums:
            return 0

        # the problem definition: the length of increase sequence at the end of index
        # base case
        dp = [1]*len(nums)

        max_length = 1
        # loop for each status: the length
        for i in range(1, len(nums)):
            # transition
            cur_num = nums[i]
            length = 1
            for j in range(i):
                prev_num = nums[j]
                if prev_num < cur_num:
                    length = max(length, dp[j]+1)
            max_length = max(max_length, length)
            dp[i] = length

        return max_length


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    res = Solution().lengthOfLIS(nums=nums)
    print(res)
