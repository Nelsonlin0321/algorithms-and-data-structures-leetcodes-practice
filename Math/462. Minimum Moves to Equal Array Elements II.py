# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/submissions/
# Runtime: 76 ms, faster than 48.58% of Python3 online submissions for Minimum Moves to Equal Array Elements II.
# Memory Usage: 15.3 MB, less than 70.94% of Python3 online submissions for Minimum Moves to Equal Array Elements II.
from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid = len(nums) // 2
        mid_num = nums[mid]
        res = 0

        for num in nums:
            res += abs(num - mid_num)
        return res


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().minMoves2(nums))
