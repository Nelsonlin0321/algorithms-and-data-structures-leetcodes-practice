class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        if len(word1) * len(word2) == 0:
            return max(len(word1), len(word2))

        row = [None for _ in range(len(word2) + 1)]

        dp = [row.copy() for _ in range(len(word1) + 1)]

        # base case

        for i in range(len(word1) + 1):
            dp[i][0] = i

        for j in range(len(word2) + 1):
            dp[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                char_1 = word1[i - 1]
                char_2 = word2[j - 1]

                if char_1 == char_2:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + 1

        return dp[-1][-1]
