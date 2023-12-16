# https://leetcode.com/problems/combinations/description/
"""
Runtime
921ms
Beats53.14%of users with Python3
Memory
64.88MB
Beats54.64%of users with Python3
"""

from typing import List


class Solution:

    def __init__(self):
        self.res = []

    def backtrack(self, n, k, start, track):

        if len(track) == k:
            self.res.append(track.copy())
            return

        for num in range(start, n):
            num += 1
            track.append(num)
            self.backtrack(n, k, num, track)
            track.pop(-1)

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtrack(n, k, 0, [])
        return self.res
