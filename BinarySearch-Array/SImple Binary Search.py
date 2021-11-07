class Solution:

    def binary_search(self, nums, target) -> int:
        # init pointers
        left = 0
        right = len(nums) - 1

        while (left <= right):
            # get the mid pointer
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:  # means the target on the left of mid
                right = mid - 1
            elif nums[mid] < target:  # means the target on the right of mid
                left = mid + 1

        return -1


if __name__ == "__main__":
    nums = [1,5,6,7,9,10,30,56]

    print(Solution().binary_search(nums,4))