from typing import List
#https://leetcode.com/problems/permutations/submissions/
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
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:

        used_dict = {num: False for num in nums}

        self.backtracking(nums, [], used_dict)
        return self.res

    def backtracking(self, nums, path, used_dict):
        if len(path) == len(nums):
            self.res.append(path.copy())

        for num in nums:
            # used ot not
            if not used_dict[num]:
                path.append(num)
                used_dict[num] = True
                self.backtracking(nums, path, used_dict)
                # unselect
                path.pop(-1)
                used_dict[num] = False


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().permute(nums))
