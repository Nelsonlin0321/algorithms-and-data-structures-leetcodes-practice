from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return 1

        dp = [1 for _ in range(len(arr))]

        res = 1
        # base case
        if arr[0] != arr[1]:
            dp[1] = 2
            res = 2

        for idx in range(2, len(arr)):
            if arr[idx] == arr[idx - 1]:  # 相等
                dp[idx] = 1
            if arr[idx] < arr[idx - 1]:  # 当前值往下
                if arr[idx - 1] > arr[idx - 2]:  # 上一个值往上
                    dp[idx] = dp[idx - 1] + 1
                else:  # 上一个值往上
                    dp[idx] = 2
            if arr[idx] > arr[idx - 1]:  # 当前值往上
                if arr[idx - 1] < arr[idx - 2]:  # 上一个值往下
                    dp[idx] = dp[idx - 1] + 1
                else:
                    dp[idx] = 2
            res = max(res, dp[idx])
        return res

# Runtime: 552 ms, faster than 19.95% of Python3 online submissions for Longest Turbulent Subarray.
# Memory Usage: 18.6 MB, less than 84.74% of Python3 online submissions for Longest Turbulent Subarray.

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return 1

        # dp = [1 for _ in range(len(arr))]

        res = 1
        prev = 1

        # base case
        if arr[0] != arr[1]:
            prev = 2

        curr = prev
        res = max(res, curr)

        for idx in range(2, len(arr)):
            if arr[idx] == arr[idx - 1]:  # 相等
                curr = 1
            if arr[idx] < arr[idx - 1]:  # 当前值往下
                if arr[idx - 1] > arr[idx - 2]:  # 上一个值往上
                    curr = prev + 1
                else:  # 上一个值往上
                    curr = 2
            if arr[idx] > arr[idx - 1]:  # 当前值往上
                if arr[idx - 1] < arr[idx - 2]:  # 上一个值往下
                    curr = prev + 1
                else:
                    curr = 2
            res = max(res, curr)
            prev = curr
        return res


if __name__ == "__main__":
    arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
    print(Solution().maxTurbulenceSize(arr))
