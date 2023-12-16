# https://leetcode.com/problems/combination-sum-iii/

"""
Runtime
40ms
Beats51.59%of users with Python3
Memory
16.46MB
Beats7.94%of users with Python3
"""


from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def backtrack(self, k, n, track, value_sum, start):
        if len(track) == k and value_sum == n:
            self.res.append(track.copy())
            return

        if value_sum > n or len(track) > k:
            return

        for num in range(start, 10):
            track.append(num)
            value_sum += num
            self.backtrack(k, n, track, value_sum, num+1)
            value_sum -= num
            track.pop(-1)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.backtrack(k, n, [], 0, 1)
        return self.res
