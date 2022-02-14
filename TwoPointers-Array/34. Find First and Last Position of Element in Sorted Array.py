from typing import List

"""
Runtime: 99 ms, faster than 58.17% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 15.5 MB, less than 55.84% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
"""


class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # left boundary

        middle = self.binarySearh(nums, target)

        if middle == -1:
            return [-1, -1]
        left = self.searchLeft(nums[:middle + 1], target)

        right = self.searchRight(nums[middle:], target)

        return [left, middle + right]

    def binarySearh(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return -1

    def searchLeft(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] == target:
                if middle == 0 or nums[middle - 1] != target:
                    return middle
                else:
                    right = middle - 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return -1

    def searchRight(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] == target:
                if middle == len(nums) - 1 or nums[middle + 1] != target:
                    return middle
                else:
                    left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return -1


if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 8

    print(Solution().searchRange(nums, target))
