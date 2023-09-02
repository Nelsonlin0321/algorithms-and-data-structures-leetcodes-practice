from typing import List
"""
Runtime
Details
1164ms
Beats 87.98%of users with Python3
Memory
Details
55.45MB
Beats 10.52%of users with Python3
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # base case
        if len(intervals) <= 0:
            return 0

        # sort
        intervals = sorted(intervals, key=lambda x: x[0])
        intervals = sorted(intervals, key=lambda x: x[1])
        i = 0
        j = 1
        num_overlap = 0
        while i < len(intervals) and j < len(intervals):

            left_interval = intervals[i]
            right_inveral = intervals[j]

            if left_interval[1] <= right_inveral[0]:
                # no overalpping
                i = j
            else:
                num_overlap += 1
            j += 1

        return num_overlap


if __name__ == "__main__":
    intervals = [[1, 2], [1, 2], [1, 2]]
    res = Solution().eraseOverlapIntervals(intervals)
    print(res)
