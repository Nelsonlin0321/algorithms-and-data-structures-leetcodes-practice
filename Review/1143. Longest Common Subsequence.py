"""
Success
Details
Runtime: 480 ms, faster than 67.04% of Python3 online submissions for Longest Common Subsequence.
Memory Usage: 22.1 MB, less than 63.70% of Python3 online submissions for Longest Common Subsequence.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # base case
        if len(text1) * len(text2) == 0:
            return 0

        rows = [0 for _ in range(len(text2) + 1)]
        dp = [rows.copy() for _ in range(len(text1) + 1)]
        # x = text1
        # y = text2

        for x in range(1, len(text1) + 1):
            for y in range(1, len(text2) + 1):
                if text1[x - 1] == text2[y - 1]:
                    # 相等的话，这两个字符串为新增
                    dp[x][y] = dp[x - 1][y - 1] + 1
                else:
                    # 不相等，当前的最长公共序列存在上一个阶段
                    dp[x][y] = max(dp[x - 1][y], dp[x][y - 1])

        return dp[-1][-1]


if __name__ == "__main__":
    text1 = "abcde"
    text2 = "ace"
    print(Solution().longestCommonSubsequence(text1, text2))
