from typing import List


class Solution():
    def binarySearch(self, nums: List[int], target: int):
        i = 0
        j = len(nums)-1

        while i <= j:
            z = i + (j-i)//2

            middle = nums[z]

            if middle == target:
                return z
            elif middle > target:
                j = z-1
            elif middle < target:
                i = z+1

        return -1


if __name__ == "__main__":
    nums = [1, 2, 3]
    target = 3
    res = Solution().binarySearch(nums, target)
    print(res)
