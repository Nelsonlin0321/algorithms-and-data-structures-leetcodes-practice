# https://leetcode.com/problems/non-decreasing-array/

from typing import List
"""
Runtime
Details
167ms
Beats 75.54%of users with Python3
Memory
Details
17.81MB
Beats 18.21%of users with Python3
"""


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        i = 0
        cnt = 0
        for i in range(0, len(nums)-1):
            left = nums[i]
            right = nums[i+1]

            if left > right:
                if i != 0:
                    if right >= nums[i-1]:
                        # change the left first
                        nums[i] = right
                    else:
                        nums[i+1] = left
                cnt += 1
                if cnt > 1:
                    return False
            i += 1
        return True


if __name__ == "__main__":
    nums = [3, 4, 2, 3]
    res = Solution().checkPossibility(nums)
    print(res)
