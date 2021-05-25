# https://leetcode.com/problems/largest-number/submissions/
# Runtime: 72 ms, faster than 16.62% of Python3 online submissions for Largest Number.
# Memory Usage: 14.4 MB, less than 27.00% of Python3 online submissions for Largest Number.
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        if len(nums) == 0:
            return 0
        str_nums = [str(num) for num in nums]

        for i in range(
                len(nums) - 1,
                0,
                -1
        ):
            for j in range(i):
                if int(str_nums[j] + str_nums[j + 1]) < int(str_nums[j + 1] + str_nums[j]):
                    str_nums[j + 1], str_nums[j] = str_nums[j], str_nums[j + 1]

        res = "".join(str_nums)
        if res[0] == "0":
            return "0"
        else:
            return res

# Runtime: 40 ms, faster than 62.87% of Python3 online submissions for Largest Number.
# Memory Usage: 14.3 MB, less than 58.81% of Python3 online submissions for Largest Number.

class Solution:
    def BubbleSort(self, str_nums: List[str]) -> str:

        if len(str_nums) == 0:
            return 0
        # str_nums = [str(num) for num in nums]

        for i in range(
                len(str_nums) - 1,
                0,
                -1
        ):
            for j in range(i):
                if int(str_nums[j] + str_nums[j + 1]) < int(str_nums[j + 1] + str_nums[j]):
                    str_nums[j + 1], str_nums[j] = str_nums[j], str_nums[j + 1]

    def largestNumber(self, nums: List[int]) -> str:

        """
        分桶：0-9
        """
        nums_list = [[] for _ in range(10)]

        for num in nums:
            idx = int(str(num)[0])
            nums_list[idx].append(str(num))

        # print(nums_list)

        for str_nums in nums_list:
            self.BubbleSort(str_nums)

        res = []
        _ = [res.extend(str_nums) for str_nums in nums_list[::-1]]
        res = "".join(res)

        if res[0] == "0":
            return "0"
        return res


if __name__ == '__main__':
    nums = [3, 30, 34, 5, 9]
    print(Solution().largestNumber(nums))
