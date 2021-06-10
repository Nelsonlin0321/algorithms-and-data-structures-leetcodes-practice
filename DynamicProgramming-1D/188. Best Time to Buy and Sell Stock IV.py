from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        k_list = [-float('-inf') for _ in range(k)]
        hold_cash = [k_list.copy() for _ in range(2)]
        dp = [hold_cash.copy() for _ in range(len(prices))]

        # base case
        if len(prices) <= 1:
            return 0

        # 0 for hold
        # 1 for cash
        # dp[ day ] [hold or cash][k]

        dp[0][0][0] = -prices[0]
        # hold
        for th in range(k):
            dp[0][1][th] = 0  # cash
            # dp[0][0][th] = -prices[0]

        for t in range(1, len(prices)):
            for th in range(k):
                # hold - > 昨天的hold， 今天买入，
                dp[t][0][th] = max(dp[t - 1][0][th], dp[t][1][th - 1] - prices[t])  # hold
                # print(dp[t][0][th])
                dp[t][1][th] = max(dp[t - 1][1][th], prices[t] + dp[t - 1][0][th])  # cash

        res = dp[-1][1][-1]

        return int(res)


k = 2
prices = [3, 2, 6, 5, 0, 3]

print(Solution().maxProfit(k, prices))
