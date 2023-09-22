from typing import List

"""
Runtime
Details
109ms
Beats 7.14%of users with Python3
Memory
Details
16.53MB
Beats 68.59%of users with Python3
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_nums = []

        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged_nums.append(nums1[i])
                i += 1
            else:
                merged_nums.append(nums2[j])
                j += 1

        while i < len(nums1):
            merged_nums.append(nums1[i])
            i += 1

        while j < len(nums2):
            merged_nums.append(nums2[j])
            j += 1

        length = len(merged_nums)
        print(merged_nums)
        mid = length//2
        if length % 2 == 1:
            return merged_nums[mid]
        else:
            return sum(merged_nums[mid-1:mid+1])/2


if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    res = Solution().findMedianSortedArrays(nums1, nums2)
    print(res)
