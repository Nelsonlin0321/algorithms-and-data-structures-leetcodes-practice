# https://leetcode.com/problems/permutations-ii/
"""
Runtime
57ms
Beats74.50%of users with Python3
Memory
16.56MB
Beats69.53%of users with Python3
"""

from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def backtracking(self, nums, path, used):
        if len(path) == len(nums):
            self.res.append(path.copy())
            return

        for i in range(len(nums)):
            if not used[i]:
                """
                判断这个数字是否与上个数字相同,假如上个数字已经用过那么当前就得pass
                """
                if i > 0 and nums[i] == nums[i - 1] and used[i - 1]:
                    continue

                used[i] = True
                path.append(nums[i])
                self.backtracking(nums, path, used)
                used[i] = False
                path.pop()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used = [False for _ in range(len(nums))]
        nums.sort()
        self.backtracking(nums, [], used)
        return self.res


class Solution:
    def __init__(self):
        self.res = []
        self.is_used = set()

    def backtrack(self, nums, track):

        if len(nums) == len(track):
            self.res.append(track.copy())
            return

        prev = float('inf')
        for i in range(len(nums)):
            num = nums[i]
            if i in self.is_used or num == prev:
                # if th num is used, to make sure it equals prev
                continue
            prev = num
            track.append(num)
            self.is_used.add(i)
            self.backtrack(nums, track)
            self.is_used.remove(i)
            track.pop(-1)

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.backtrack(nums, [])
        return self.res


if __name__ == "__main__":
    nums = [2, 2, 1, 1]
    print(Solution().permuteUnique(nums))
