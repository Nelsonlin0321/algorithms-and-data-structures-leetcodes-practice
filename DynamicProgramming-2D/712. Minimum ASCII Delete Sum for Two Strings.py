"""
Success
Details
Runtime: 987 ms, faster than 54.25% of Python3 online submissions for Minimum ASCII Delete Sum for Two Strings.
Memory Usage: 18.7 MB, less than 54.07% of Python3 online submissions for Minimum ASCII Delete Sum for Two Strings.
"""

class Solution:

    def helper(self, string):
        sum_ascii = 0
        for char in string:
            sum_ascii += ord(char)
        return sum_ascii

    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        # base case

        if len(s1) * len(s2) == 0:
            return self.helper(s1) + self.helper(s2)

        row = [None for _ in range(len(s2) + 1)]
        dp = [row.copy() for _ in range(len(s1) + 1)]

        # base case

        for i in range(len(s1) + 1):
            dp[i][0] = self.helper(s1[:i])

        for j in range(len(s2) + 1):
            dp[0][j] = self.helper(s2[:j])

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                char_1 = s1[i - 1]
                char_2 = s2[j - 1]

                if char_1 == char_2:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i][j - 1] + ord(s2[j - 1]),
                        dp[i - 1][j] + ord(s1[i - 1])
                    )
        return dp[-1][-1]




