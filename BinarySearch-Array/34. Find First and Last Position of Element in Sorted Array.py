from typing import List
# Runtime: 80 ms, faster than 88.01% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
# Memory Usage: 15.6 MB, less than 8.85% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.

class Solution:

    def left_idx_search(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                if mid == 0 or nums[mid - 1] != target:
                    return mid
                else:
                    high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1

        return -1

    def right_idx_search(self, start, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    return mid + start
                else:
                    low = mid + 1
            elif target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1

        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # base case

        if len(nums) == 0:
            return [-1, -1]

        low = 0
        high = len(nums) - 1

        res = []

        while low <= high:

            mid = low + (high - low) // 2

            if nums[mid] == target:

                # 判断是是否为左边界
                if mid == 0 or nums[mid - 1] != target:
                    res.append(mid)  # # 判断是是否为左边界
                else:
                    res.append(self.left_idx_search(nums[:mid], target))

                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    res.append(mid)
                else:
                    res.append(self.right_idx_search(mid + 1, nums[mid + 1:], target))

                if len(res) == 2:
                    return res

            elif target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1

        return [-1, -1]


if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 8, 8, 10]
    target = 8
    print(Solution().searchRange(nums, 8))
