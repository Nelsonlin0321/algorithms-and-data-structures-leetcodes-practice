
class Solution:

    def binary_search(self, nums, target) -> bool:
        low = 0
        high = len(nums) - 1

        while (low <= high):  # if target 在high 的位置的话， 那么 low 会减1， 与 high 相等，此时 mid = left = high
            mid = low + (high - low) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
        return -1


if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    nums = [5, 6, 7, 8, 10]
    print(Solution().binary_search(nums, 8))
