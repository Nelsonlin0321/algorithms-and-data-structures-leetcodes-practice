# https://leetcode.com/problems/permutations-ii/
# Runtime: 92 ms, faster than 29.73% of Python3 online submissions for Permutations II.
# Memory Usage: 14.6 MB, less than 56.27% of Python3 online submissions for Permutations II.

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
                判断这个数字是否与上个数字相同，假如上个数字已经用过那么当前就得pass
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


if __name__ == "__main__":
    nums = [2, 2, 1, 1]
    print(Solution().permuteUnique(nums))
