# https://leetcode.com/problems/subsets-ii/
"""
Runtime
40ms
Beats77.73%of users with Python3
Memory
16.38MB
Beats92.35%of users with Python3
"""


from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def backtrack(self, nums, track, start):
        self.res.append(track.copy())

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            num = nums[i]
            track.append(num)
            self.backtrack(nums, track, i+1)
            track.pop(-1)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.backtrack(nums, [], 0)
        return self.res
