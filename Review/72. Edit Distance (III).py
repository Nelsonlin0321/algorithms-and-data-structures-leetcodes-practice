"""
Success
Details
Runtime: 287 ms, faster than 22.54% of Python3 online submissions for Edit Distance.
Memory Usage: 17.4 MB, less than 73.63% of Python3 online submissions for Edit Distance.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        default_distance = max(len(word1), len(word2))

        # base case
        if len(word1) * len(word2) == 0:
            return default_distance

        # dp table
        row = [default_distance for _ in range(len(word2) + 1)]
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
                    # 相同的情况上，就不用操作，就等于上一个阶段
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 不相同的情况上，有三种操作的可能 1）删除左边 2） 删除右边 3）替换
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

        return dp[-1][-1]
