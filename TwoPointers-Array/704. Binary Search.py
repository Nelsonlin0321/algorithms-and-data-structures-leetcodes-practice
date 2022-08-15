from typing import List
# https://leetcode.com/problems/binary-search/submissions/
"""
Runtime: 367 ms, faster than 35.08% of Python3 online submissions for Binary Search.
Memory Usage: 15.3 MB, less than 98.97% of Python3 online submissions for Binary Search.
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right: #[Important!]: When to stop the while loop
            # [Important!]: How to get the middle index
            middle = left + (right - left) // 2

            if nums[middle] == target:
                return middle

            elif nums[middle] > target:
                right = middle - 1

            elif nums[middle] < target:
                left = middle + 1
        # [Important!]: After couldn't find it by binary search
        return - 1


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9

    print(Solution().search(nums, target))
