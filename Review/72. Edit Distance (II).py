# https://leetcode.com/problems/edit-distance/

"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
"""

""""
Success
Details 
Runtime: 226 ms, faster than 16.60% of Python3 online submissions for Edit Distance.
Memory Usage: 18 MB, less than 15.73% of Python3 online submissions for Edit Distance.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        if m * n == 0:
            return m + n

        # initiate

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # dp[word1][word2]

        # base case : important the imagine the dp table
        for i in range(m + 1):
            dp[i][0] = i

        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 对单词 A 删除一个字符和对单词 B 插入一个字符是等价的
                    delete_left = dp[i - 1][j]
                    delete_right = dp[i][j - 1]
                    replace = dp[i - 1][j - 1]
                    dp[i][j] = 1 + min(delete_left, delete_right, replace)

        return dp[-1][-1]


if __name__ == "__main__":
    word1 = "horse"
    word2 = "ros"

    print(Solution().minDistance(word1, word2))
