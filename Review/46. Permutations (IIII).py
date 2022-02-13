from typing import List

"""
https://leetcode.com/problems/permutations/
"""

"""
Runtime: 58 ms, faster than 43.83% of Python3 online submissions for Permutations.
Memory Usage: 14 MB, less than 89.29% of Python3 online submissions for Permutations.
"""


class Solution:
    def __init__(self):
        self.paths = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        used_dict = {num: False for num in nums}
        path = []
        self.backtrack(path, nums, used_dict)
        return self.paths

    def backtrack(self, path, nums, used_dict):
        if len(path) == len(nums):
            self.paths.append(path.copy())
            return

        for num in nums:
            if not used_dict[num]:
                # select
                path.append(num)
                used_dict[num] = True
                # backtrack
                self.backtrack(path, nums, used_dict)
                # unselect
                used_dict[num] = False
                path.pop(-1)


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().permute(nums))
