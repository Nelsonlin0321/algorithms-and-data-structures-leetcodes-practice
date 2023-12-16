# https://leetcode.com/problems/combination-sum/
"""
Runtime
64ms
Beats46.96%of users with Python3
Memory
16.49MB
Beats41.50%of users with Python3
"""


from typing import List


class Solution:

    def __init__(self):
        self.res = []

    def backtrack(self, candidates, target, track, value_sum, start):
        if value_sum == target:
            self.res.append(track.copy())
            return

        if value_sum > target:
            return

        for i in range(start, len(candidates)):
            num = candidates[i]
            value_sum += num
            track.append(num)
            self.backtrack(candidates, target, track, value_sum, i)
            value_sum -= num
            track.pop(-1)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.backtrack(candidates, target, [], 0, 0)
        return self.res
