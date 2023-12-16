# https://leetcode.com/problems/subsets/description/
"""
Runtime
53ms
Beats5.65%of users with Python3
Memory
16.53MB
Beats28.33%of users with Python3
"""


from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def backtrack(self, nums, track, start):
        self.res.append(track.copy())

        for i in range(start, len(nums)):
            num = nums[i]
            track.append(num)
            self.backtrack(nums, track, i+1)
            track.pop(-1)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, [], 0)
        return self.res
