from typing import List


class Solution:

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        envelopes = sorted(envelopes, key=lambda x: x[0] * x[1])

        dp = [1 for _ in range(len(envelopes))]

        max_envelopes = 1

        for i in range(1, len(envelopes)):
            max_env = 1
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    max_env = max(max_env, dp[j] + 1)

            dp[i] = max_env
            max_envelopes = max(max_envelopes, max_env)

        return max_envelopes


if __name__ == "__main__":
    envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
    # envelopes = [[1, 1], [1, 1], [1, 1]]

    print(Solution().maxEnvelopes(envelopes))
