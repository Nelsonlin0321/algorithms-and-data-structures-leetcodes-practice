"""
Success
Details
Runtime: 637 ms, faster than 93.26% of Python3 online submissions for Minimum Insertion Steps to Make a String Palindrome.
Memory Usage: 16.2 MB, less than 47.95% of Python3 online submissions for Minimum Insertion Steps to Make a String Palindrome.
"""


class Solution:
    def minInsertions(self, s: str) -> int:

        row = [0 for _ in range(len(s))]
        dp = [row.copy() for _ in range(len(s))]

        # base case

        for i in range(len(s)):
            dp[i][i] = 0

        for i in range(len(s) - 1, -1, -1):  # start
            for j in range(i + 1, len(s)):  # end

                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1

        return dp[0][-1]


if __name__ == "__main__":
    s = "zzazz"
    print(Solution().minInsertions(s))
