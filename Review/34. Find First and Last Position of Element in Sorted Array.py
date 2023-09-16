"""
Runtime
Details
90ms
Beats 32.28%of users with Python3
Memory
Details
17.82MB
Beats 24.23%of users with Python3
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        i = 0
        j = len(nums)-1

        left = -1
        right = -1
        while i <= j:
            z = i+(j-i)//2
            mid = nums[z]

            if mid > target:
                j = z - 1

            if mid < target:
                i = z + 1

            if mid == target:
                if z == 0 or nums[z-1] != target:
                    left = z
                    break
                else:
                    j = z-1

        if left != -1:
            for right in range(left, len(nums)):
                if nums[right] == target:
                    if right == len(nums)-1 or nums[right+1] != target:
                        break
        return [left, right]


if __name__ == "__main__":
    nums = [1]
    target = 1
    res = Solution().searchRange(nums, target)
    print(res)
