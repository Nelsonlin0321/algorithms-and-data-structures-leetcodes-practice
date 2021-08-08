from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        path = []
        self.backtrack(nums, path, 0)
        return self.res

    def permute(self, nums: List[int]) -> List[List[int]]:
        used_dict = {idx: False for idx in range(len(nums))}
        path = []
        self.backtrack(nums, path, used_dict)
        return self.res

    def backtrack(self, nums, path, used_dict):
        """ 排列：元素个数一样，但是顺序不一致"""
        if len(path) == len(nums):
            self.res.append(path.copy())

        for idx, num in enumerate(nums):
            if not used_dict[idx]:
                path.append(num)
                used_dict[idx] = True
                self.backtrack(nums, path, used_dict)
                path.pop(-1)
                used_dict[idx] = False


"""
Runtime: 108 ms, faster than 30.50% of Python3 online submissions for Permutations II.
Memory Usage: 14.4 MB, less than 78.58% of Python3 online submissions for Permutations II.
"""

class Solution:
    def __init__(self):
        self.res = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """sort to avoid recalculatiing """
        nums.sort()
        path = []
        used_dict = {idx: False for idx in range(len(nums))}

        self.backtrack(nums, path, used_dict)
        return self.res

    def backtrack(self, nums, path, used_dict):
        """ 排列：元素个数一样，但是顺序不一致"""
        if len(path) == len(nums):
            self.res.append(path.copy())
            return

        for idx, num in enumerate(nums):

            if not used_dict[idx]:
                """
                !!!!!!判断这个数字是否与上个数字相同，假如上个数字已经用过!!! 那么当前就得pass
                """
                if idx > 0 and nums[idx] == nums[idx - 1] and used_dict[idx- 1]:
                    continue

                path.append(num)
                used_dict[idx] = True
                self.backtrack(nums, path, used_dict)
                path.pop(-1)
                used_dict[idx] = False


if __name__ == "__main__":
    nums = [1, 1, 3]
    print(Solution().permuteUnique(nums))
