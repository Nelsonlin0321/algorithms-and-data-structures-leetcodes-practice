from typing import List
import numpy as np
from utils import random_question


# print(random_question()) # QuickSort.py

class Solution:

    def QuickSort(self, nums: List[int]):

        left = 0
        right = len(nums) - 1
        self._QuickSort(nums, left, right)

    def partition(self, nums, left, right):

        pivot = nums[right]
        while left < right:

            while left < right and nums[left] <= pivot:
                left += 1

            nums[right] = nums[left]

            while left < right and nums[right] > pivot:
                right -= 1

            nums[left] = nums[right]

        res_idx = right
        nums[res_idx] = pivot
        return res_idx

    def _QuickSort(self, nums, left, right):
        # recursive
        if left < right:
            pivot = self.partition(nums, left, right)
            self._QuickSort(nums, left, pivot - 1)
            self._QuickSort(nums, pivot + 1,right )


print("Before Being Sorted")
nums = np.random.randint(0,20,10)
print(nums)
print("After Being Sorted")
Solution().QuickSort(nums)
print(nums)



