"""
215. Kth Largest Element in an Array
Medium

5903

370

Add to List

Share
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Constraints:

1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104
"""


class Solution(object):

    """
    Runtime: 992 ms, faster than 12.38% of Python online submissions for Kth Largest Element in an Array.
    Memory Usage: 17.7 MB, less than 8.17% of Python online submissions for Kth Largest Element in an Array.
    """

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        #  convert k to the index
        # len(array)+1 = idex + k
        target_index = len(nums) - k

        left = 0
        right = len(nums) - 1

        return self.recursive_partition(nums, left, right, target_index)

    def recursive_partition(self, nums, left, right, target_index):

        pivot = self.partition(nums, left, right)

        if pivot == target_index:  # conquer
            return nums[target_index]
        elif pivot > target_index: # divide
            return self.recursive_partition(nums, left, pivot - 1, target_index)
        elif pivot < target_index:
            return self.recursive_partition(nums, pivot + 1,right, target_index)
        # no need to combine

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


if __name__ == "__main__":
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(Solution().findKthLargest(nums, k))
