from typing import List

"""
Runtime: 5607 ms, faster than 12.84% of Python3 online submissions for Two Sum.
Memory Usage: 15 MB, less than 63.86% of Python3 online submissions for Two Sum.
"""

"""
时间复杂度 O(N^2)，空间复杂度 O(1)。
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for left in range(len(nums)):
            for right in range(left + 1, len(nums)):
                if nums[left] + nums[right] == target:
                    return [left, right]


"""
Runtime: 73 ms, faster than 72.87% of Python3 online submissions for Two Sum.
Memory Usage: 15.3 MB, less than 34.79% of Python3 online submissions for Two Sum.
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash_dict
        hash_dict = {num: index for (index, num) in enumerate(nums)} # 使用哈希字典来减少索引时间

        for (index, num) in enumerate(nums):
            remain = target - num
            if remain in hash_dict:
                if hash_dict[remain] != index:
                    return [hash_dict[remain], index]
