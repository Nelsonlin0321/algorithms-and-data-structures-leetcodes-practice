"""
Success
Details
Runtime: 1962 ms, faster than 62.48% of Python3 online submissions for Longest Palindromic Subsequence.
Memory Usage: 30.6 MB, less than 83.13% of Python3 online submissions for Longest Palindromic Subsequence.
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # base case
        if len(s) == 0:
            return 0

        row = [0 for _ in range(len(s))]
        dp = [row.copy() for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1

        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):

                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][-1]


if __name__ == "__main__":
    s = "bbbab"
    print(Solution().longestPalindromeSubseq(s))
