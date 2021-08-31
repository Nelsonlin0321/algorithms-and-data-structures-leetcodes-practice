from typing import List

"""
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


class Solution:

    def __init__(self):
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:

        used_dict = {num: False for num in nums}
        self.backtrack(nums, [], used_dict)
        return self.res

    def backtrack(self, nums, path, used_dict):

        if len(path) == len(nums):
            self.res.append(path.copy())
            return

        for num in nums:
            if used_dict[num]:
                continue

            path.append(num)
            used_dict[num] = True
            self.backtrack(nums, path, used_dict)
            # unselected
            path.pop(-1)
            used_dict[num] = False


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().permute(nums))
