# https://leetcode.com/problems/permutations/submissions/
# Runtime: 32 ms, faster than 95.89% of Python3 online submissions for Permutations.
# Memory Usage: 14.5 MB, less than 41.63% of Python3 online submissions for Permutations.

from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def backtracking(self, nums, path, used_item):

        if len(path) == len(nums):
            """
            满足条件进行储存回撤
            """
            self.res.append(path.copy())
            return

        for i in range(len(nums)):
            if not used_item[i]:  # 当这个元素没有被使用的话
                # 选择
                path.append(nums[i])
                used_item[i] = True
                # 继续迭代
                self.backtracking(nums, path, used_item)
                # 取消选择
                path.pop()
                used_item[i] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        used_item = [False for _ in range(len(nums))]

        self.backtracking(nums, [], used_item)

        return self.res

# Runtime: 36 ms, faster than 86.20% of Python3 online submissions for Permutations.
# Memory Usage: 14.4 MB, less than 41.63% of Python3 online submissions for Permutations.

class Solution:
    def __init__(self):
        self.res = []

    def backtracking(self, nums, k):

        if k == len(nums):
            """
            满足条件进行储存回撤
            """
            self.res.append(nums.copy())
            return

        for i in range(k, len(nums)):
            # switch the position to be the first letter to continue
            nums[i], nums[k] = nums[k], nums[i]
            self.backtracking(nums, k + 1)
            nums[i], nums[k] = nums[k], nums[i]

    def permute(self, nums: List[int]) -> List[List[int]]:

        self.backtracking(nums, 0)

        return self.res


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().permute(nums))
