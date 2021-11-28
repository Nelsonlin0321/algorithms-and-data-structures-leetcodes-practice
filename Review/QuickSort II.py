from typing import List
import numpy as np
from utils import random_question


# print(random_question()) # QuickSort.py

class Solution:

    def QuickSort(self, nums: List[int]):
        self.recursive_partition(nums, 0, len(nums) - 1)

    def recursive_partition(self, nums, left, right):
        if left < right:
            pivot = self.partition(nums, left, right)
            self.recursive_partition(nums, pivot + 1, right)
            self.recursive_partition(nums, left, pivot - 1)

    def partition(self, nums, left, right):
        pivot = nums[right]

        while left < right:
            while left < right and nums[left] <= pivot:
                left += 1

            nums[right] = nums[left]

            while left < right and nums[right] > pivot:
                right -= 1

            nums[left] = nums[right]

        nums[right] = pivot

        return right


print("Before Being Sorted")
nums = np.random.randint(0, 20, 10)
print(nums)
print("After Being Sorted")
Solution().QuickSort(nums)
print(nums)
