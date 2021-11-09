# https://leetcode.com/problems/merge-sorted-array/
from typing import List

#  不过细心
"""
Runtime: 36 ms, faster than 77.68% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 14.2 MB, less than 62.45% of Python3 online submissions for Merge Sorted Array.
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        curr = len(nums1) - 1
        left = m - 1
        right = n - 1

        while (curr != -1):

            if left != -1 and right != -1:
                left_num = nums1[left]
                right_num = nums2[right]

                if left_num <= right_num:
                    right -= 1
                    nums1[curr] = right_num

                elif left_num > right_num:
                    left -= 1
                    nums1[curr] = left_num

            elif right != -1:
                right_num = nums2[right]
                right -= 1
                nums1[curr] = right_num

            elif left != -1:
                left_num = nums1[left]
                left -= 1
                nums1[curr] = left_num

            curr -= 1
