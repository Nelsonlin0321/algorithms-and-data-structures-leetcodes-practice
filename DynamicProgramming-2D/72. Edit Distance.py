class Solution:
    """
    Runtime: 160 ms, faster than 75.79% of Python3 online submissions for Edit Distance.
    Memory Usage: 17.9 MB, less than 21.47% of Python3 online submissions for Edit Distance.
    """

    def minDistance(self, word1: str, word2: str) -> int:
        # base case
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))

        row = [None for _ in range(len(word2) + 1)]
        dp = [row.copy() for _ in range(len(word1) + 1)]
        # dp [word1][word2]

        # base case
        for word_1_idx in range(len(word1) + 1):
            dp[word_1_idx][0] = word_1_idx

        for word_2_idx in range(len(word2) + 1):
            dp[0][word_2_idx] = word_2_idx

        for word_1_idx in range(1, len(word1) + 1):
            for word_2_idx in range(1, len(word2) + 1):
                if word1[word_1_idx - 1] == word2[word_2_idx - 1]:
                    dp[word_1_idx][word_2_idx] = dp[word_1_idx - 1][word_2_idx - 1]
                else:
                    # 替换-> 左替换， 右替换
                    # 删除 -
                    dp[word_1_idx][word_2_idx] = 1 + min(dp[word_1_idx][word_2_idx - 1],  # 右边删除
                                                         dp[word_1_idx - 1][word_2_idx],  # 左边删除
                                                         dp[word_1_idx - 1][word_2_idx - 1],  # 替换
                                                         )

        return dp[-1][-1]


word1 = "intention"
word2 = "execution"
print(Solution().minDistance(word1, word2))
