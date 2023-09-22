from typing import List

"""
Runtime
Details
61ms
Beats 35.12%of users with Python3
Memory
Details
16.74MB
Beats 94.90%of users with Python3
"""


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums)-1

        while start <= end:
            mid = start + (end-start)//2
            mid_num = nums[mid]

            low = nums[start]
            high = nums[end]
            if mid_num == target:
                return True

            if low != high:
                if mid_num <= high:
                    # the right is sorted, to see if the target num in the right
                    if mid_num < target <= high:
                        start = mid+1
                    else:
                        end = mid-1
                elif mid_num >= low:
                    # the left part is sorted, to see if the target num in the left
                    if low <= target < mid_num:
                        end = mid-1
                    else:
                        start = mid+1
            else:
                start += 1

        return False


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 2, 0]
    target = 2
    res = Solution().search(nums, target)
    print(res)
