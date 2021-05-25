class Solution(object):

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

    def recursive_partition(self, nums, left, right):
        if left < right:
            pivot = self.partition(nums, left, right)
            self.recursive_partition(nums, left, pivot - 1)
            self.recursive_partition(nums, pivot + 1, right)

    def QuickSort(self, nums):
        left = 0
        right = len(nums) - 1
        self.recursive_partition(nums, left, right)


if __name__ == "__main__":
    nums = [1, 8, 5, 6, 2, 2, 3, 5, 6, 67]
    Solution().QuickSort(nums)
    print(nums)
