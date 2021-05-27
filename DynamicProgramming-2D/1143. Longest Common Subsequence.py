import numpy as np
# Runtime: 536 ms, faster than 32.13% of Python3 online submissions for Longest Common Subsequence.
# Memory Usage: 21.9 MB, less than 80.91% of Python3 online submissions for Longest Common Subsequence.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res = 0
        # base case
        if len(text1) == 0 or len(text2) == 0:
            return res

        arr = [0 for _ in range(len(text2))]
        dp = [arr.copy() for _ in range(len(text1))]

        # dp[text_1_idx][text_2_idx]

        # base case
        if text1[0] == text2[0]:
            dp[0][0] = 1

        for idx in range(len(text1)):
            if text2[0] in text1[:idx + 1]:
                dp[idx][0] = 1
                res = 1
            else:
                dp[idx][0] = 0

        for idx in range(len(text2)):
            if text1[0] in text2[:idx + 1]:
                dp[0][idx] = 1
                res = 1
            else:
                dp[0][idx] = 0

        for idx in range(1, len(text1)):
            for jdx in range(1, len(text2)):
                if text1[idx] == text2[jdx]:
                    dp[idx][jdx] = dp[idx - 1][jdx - 1] + 1

                else:
                    dp[idx][jdx] = max(dp[idx][jdx - 1], dp[idx - 1][jdx])
                res = max(dp[idx][jdx], res)
        # print(np.array(dp))
        return res


if __name__ == "__main__":
    text1 = "xaxx"
    text2 = "a"
    print(Solution().longestCommonSubsequence(text1, text2))
