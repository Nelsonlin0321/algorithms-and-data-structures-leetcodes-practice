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


"""
Runtime: 3319 ms, faster than 59.45% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage: 14.2 MB, less than 47.61% of Python3 online submissions for Longest Increasing Subsequence.
"""


"""
子问题的定义跟一般的不一样：
1） 以i指针为结尾的最大子序列 无法 以推导出 i+1指针为结尾的最大子序列
2） 我们的定义是这样的：dp[i] 表示以 nums[i] 这个数结尾的最长递增子序列的长度。
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1 for _ in range(len(nums))]
        
        max_len = 1
        for i in range(1,len(nums)):
            curr = nums[i]
            curr_max = 1
            for j in range(0,i):
                prev = nums[j]
                if prev < curr:
                    curr_max = max(curr_max,dp[j]+1)
            dp[i] = curr_max
            max_len = max(max_len,curr_max)

        return max_len


if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    nums = [0,1,0,3,2,3]
    nums = [7,7,7,7,7,7,7]
    print(Solution().lengthOfLIS(nums=nums))
    
            
                    
                     
            
        