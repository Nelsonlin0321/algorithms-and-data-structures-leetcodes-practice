from typing import List


# Wrong
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         slow = len(nums)-1  # on the right of slow, store 0
#         fast = slow  # on the left of fast to loop each val

#         while fast >= 0:

#             if nums[fast] != 0:
#                 fast -= 1
#                 slow -= 1
#             else:
#                 nums[slow], nums[fast] = nums[fast], nums[slow]
#                 fast -= 1
#                 slow -= 1

"""
Runtime
Details
150ms
Beats 46.41%of users with Python3
Memory
Details
17.93MB
Beats 40.22%of users with Python3
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0  # on the left, store non-zero values
        fast = 0  # to loop the each vals

        while fast < len(nums):

            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

            fast += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
