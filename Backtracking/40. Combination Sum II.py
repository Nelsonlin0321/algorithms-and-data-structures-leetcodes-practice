# https://leetcode.com/problems/combination-sum-ii/
"""
Runtime
69ms
Beats68.61%of users with Python3
Memory
16.47MB
Beats37.38%of users with Python3
"""
from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def backtrack(self, candidates, target, track, track_sum, start):

        if track_sum == target:
            self.res.append(track.copy())
            return

        if track_sum > target:
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            num = candidates[i]
            track.append(num)
            track_sum += num
            self.backtrack(candidates, target, track, track_sum, i+1)
            track.pop(-1)
            track_sum -= num

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.backtrack(candidates, target, [], 0, 0)
        return self.res


class Solution:
    def __init__(self):
        self.res = []

    def backtrack(self, candidates, target, track, track_sum, start):

        if track_sum == target:
            self.res.append(track.copy())
            return

        if track_sum > target:
            return

        prev = None
        for i in range(start, len(candidates)):
            num = candidates[i]
            if num == prev:
                continue
            prev = num
            track.append(num)
            track_sum += num
            self.backtrack(candidates, target, track, track_sum, i+1)
            track.pop(-1)
            track_sum -= num

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.backtrack(candidates, target, [], 0, 0)
        return self.res
