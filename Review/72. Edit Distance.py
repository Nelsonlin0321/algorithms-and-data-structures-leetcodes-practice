# https://leetcode.com/problems/edit-distance/

"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
"""

""""
Runtime: 200 ms, faster than 34.70% of Python3 online submissions for Edit Distance.
Memory Usage: 17.7 MB, less than 61.63% of Python3 online submissions for Edit Distance.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))

        dp_1 = [None for _ in range(len(word2) + 1)]

        dp = [dp_1.copy() for _ in range(len(word1) + 1)]

        # base case # important !!!,  = max(len(word1),len(word2))
        for wd1_id in range(len(word1) + 1):
            dp[wd1_id][0] = wd1_id

        for wd2_id in range(len(word2) + 1):
            dp[0][wd2_id] = wd2_id

        for wd1_id in range(1, len(word1) + 1):
            for wd2_id in range(1, len(word2) + 1):
                w1_char = word1[wd1_id - 1]
                w2_char = word1[wd2_id - 1]

                # condition
                if w1_char == w2_char:
                    dp[wd1_id][wd2_id] = dp[wd1_id - 1][wd2_id - 1]
                else:
                    ## important !!!
                    dp[wd1_id][wd2_id] = 1 + min([
                        dp[wd1_id - 1][wd2_id],
                        dp[wd1_id][wd2_id - 1],
                        dp[wd1_id - 1][wd2_id - 1]
                    ]
                    )

        return dp[-1][-1]


word1 = "horse"
word2 = "ros"

print(Solution().minDistance(word1, word2))
