from queue import PriorityQueue
from typing import List
"""
Accepted
30 / 30 testcases passed
Nelson Lin
Nelson Lin
submitted at May 13, 2025 23:46
Runtime
626ms
Beats5.06%
Analyze Complexity
Memory
45.12MB
Beats6.25%
"""


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = PriorityQueue()

        for i in range(len(nums1)):
            pq.put((nums1[i]+nums2[0], i, 0))

        result = []
        cnt = 0
        while not pq.empty():
            _, i, j = pq.get()
            if cnt == k:
                return result
            result.append([nums1[i], nums2[j]])
            j += 1
            if j < len(nums2):
                pq.put((nums1[i]+nums2[j], i, j))
            cnt += 1

        return result
