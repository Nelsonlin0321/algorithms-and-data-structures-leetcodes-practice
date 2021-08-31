from typing import List

"""
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


class Solution:

    def __init__(self):
        self.res = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ### sorted because  if not we cannot know this is the repulicated
        nums.sort()
        used_dict = {index: False for index in range(len(nums))}
        self.backtrack(nums, [], used_dict)
        return self.res

    def backtrack(self, nums, path, used_dict):

        if len(path) == len(nums):
            self.res.append(path.copy())
            return

        for (index, num) in enumerate(nums):
            if used_dict[index] or (index > 0 and nums[index] == nums[index - 1] and used_dict[index - 1]):
                continue

            path.append(num)
            used_dict[index] = True
            self.backtrack(nums, path, used_dict)
            # unselected
            path.pop(-1)
            used_dict[index] = False


if __name__ == "__main__":
    nums = [1,1,2]
    print(Solution().permuteUnique(nums))
