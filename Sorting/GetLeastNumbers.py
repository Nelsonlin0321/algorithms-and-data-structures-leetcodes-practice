class Solution(object):

    def getLeastNumber(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        #  convert k to the index
        # len(array)+1 = idex + k
        target_index = k - 1

        left = 0
        right = len(nums) - 1

        return self.recursive_partition(nums, left, right, target_index)

    def recursive_partition(self, nums, left, right, target_index):

        pivot = self.partition(nums, left, right)

        if pivot == target_index:  # conquer
            return nums[:target_index + 1]
        elif pivot > target_index:  # divide
            return self.recursive_partition(nums, left, pivot - 1, target_index)
        elif pivot < target_index:
            return self.recursive_partition(nums, pivot + 1, right, target_index)
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
    k = 5
    print(Solution().getLeastNumber(nums, k))
