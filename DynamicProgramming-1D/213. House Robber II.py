from typing import List


class Solution:

    """"
    Runtime: 28 ms, faster than 86.91% of Python3 online submissions for House Robber II.
    Memory Usage: 14.5 MB, less than 21.28% of Python3 online submissions for House Robber II.
    """

    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)

        head_nums = nums[:-1]
        tail_nums = nums[1:]

        dp_head = [0 for _ in range(len(head_nums))]
        dp_head[0] = head_nums[0]
        dp_head[1] = max(head_nums[0], head_nums[1])

        dp_tail = [0 for _ in range(len(tail_nums))]
        dp_tail[0] = tail_nums[0]
        dp_tail[1] = max(tail_nums[0], tail_nums[1])

        for t in range(2, len(nums) - 1):
            dp_head[t] = max(dp_head[t - 2] + head_nums[t], dp_head[t - 1])
            dp_tail[t] = max(dp_tail[t - 2] + tail_nums[t], dp_tail[t - 1])

        return max(dp_head[-1], dp_tail[-1])


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(Solution().rob(nums))
