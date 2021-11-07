from typing import List
"""
Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

"""
Runtime: 36 ms, faster than 91.03% of Python3 online submissions for Permutations.
Memory Usage: 14.6 MB, less than 15.29% of Python3 online submissions for Permutations.
"""

class Solution:
    def __init__(self):
        self.res_path = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        used_dict = {i: False for i in range(len(nums))}
        path = []
        self.backtracking(nums, path, used_dict)
        return self.res_path

    def backtracking(self, nums, path, used_dict):
        if len(path) == len(nums):
            self.res_path.append(path.copy())
            return

        for i in range(len(nums)):
            if not used_dict[i]:
                num = nums[i]
                # select
                path.append(num)
                used_dict[i] = True
                self.backtracking(nums, path, used_dict)
                # unselected
                _ = path.pop(-1)
                used_dict[i] = False








