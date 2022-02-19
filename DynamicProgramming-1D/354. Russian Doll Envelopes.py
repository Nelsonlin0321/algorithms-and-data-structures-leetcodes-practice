from typing import List


class Solution:

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        # sorted
        # # Time Limit Exceeded 83 / 87 test cases passed.
        # for i in range(len(envelopes) - 1, -1, -1):
        #     for j in range(i):  # not include i
        #         first = envelopes[j + 1]
        #         second = envelopes[j]
        #
        #         if first[0] * first[1] < second[0] * second[1]:
        #             envelopes[j + 1] = second
        #             envelopes[j] = first

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
