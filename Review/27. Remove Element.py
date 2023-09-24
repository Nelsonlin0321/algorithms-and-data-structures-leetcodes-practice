from typing import List

"""
Runtime
Details
43ms
Beats 44.97%of users with Python3
Memory
Details
16.32MB
Beats 26.95%of users with Python3
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # base case
        if not nums:
            return 0

        slow = 0  # the left of slow, the vals not equal to val
        fast = 0  # the right of fast, the val to be judged

        while fast < len(nums):
            if nums[fast] == val:
                fast += 1
            else:
                nums[slow] = nums[fast]
                fast += 1
                slow += 1

        return slow


if __name__ == "__main__":
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    res = Solution().removeElement(nums, val)
    print(res)
