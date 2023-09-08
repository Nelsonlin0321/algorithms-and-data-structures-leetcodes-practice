"""
Runtime
Details
92ms
Beats 15.75%of users with Python3
Memory
Details
16.24MB
Beats 78.66%of users with Python3
"""


def is_qualified(nums):
    match_suffix = {"25", "50", "75", "00"}
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            suffix = nums[i]+nums[j]
            if suffix in match_suffix:
                return True
    return False


class Solution:
    def minimumOperations(self, num: str) -> int:

        if len(num) == 1:
            if num == '0':
                return 0
            else:
                return 1

        if len(num) == 2:
            if num in {"25", "50", "75"}:
                return 0
            if num[-1] == "0":
                return 1

        check_suffix = {"2", "5", "0", "7"}
        for i in range(len(num)-2, -1, -1):
            n = num[i]
            if n in check_suffix:
                sub_num = num[i:]
                if is_qualified(sub_num):
                    return len(sub_num) - 2

        if "0" in num:
            return len(num)-1
        else:
            return len(num)


if __name__ == "__main__":
    res = Solution().minimumOperations(num="2245047")
    print(res)
