from typing import List
"""
Runtime
Details
43ms
Beats 71.89%of users with Python3
Memory
Details
16.47MB
Beats 15.20%of users with Python3
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        length = len(nums1)
        z = length-1

        while 0 <= i < length and 0 <= j < length:
            left = nums1[i]
            right = nums2[j]

            if right >= left:
                nums1[z] = right
                j -= 1
            elif left > right:
                nums1[z] = left
                i -= 1

            z -= 1

        nums1[:j+1] = nums2[:j+1]


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    Solution().merge(nums1, m, nums2, n)
