from typing import List


class Solution:
    """
    Runtime: 32 ms, faster than 97.03% of Python3 online submissions for Permutations.
    Memory Usage: 14.5 MB, less than 14.52% of Python3 online submissions for Permutations.
    """
    def __init__(self):
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:

        used = {num: False for num in nums}
        path = []
        self.backtracking(nums, used, path)

        return self.res

    def backtracking(self, nums, used, path):

        # append to the res
        if len(path) == len(nums):
            self.res.append(path.copy())
            return

        for num in nums:
            if not used[num]:
                used[num] = True
                path.append(num)
                self.backtracking(nums, used, path)
                path.pop(-1)
                used[num] = False


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().permute(nums))
