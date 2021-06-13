from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        k_list = [-float('-inf') for _ in range(k)]
        hold_cash = [k_list.copy() for _ in range(2)]
        dp = [hold_cash.copy() for _ in range(len(prices))]

        # base case
        if len(prices) <= 1:
            return 0

        res = 0

        # 1 for hold
        # 0 for cash
        # dp[ day ] [hold or cash][k]

        dp[0][1][0] = -prices[0]

        # hold
        for k_th in range(k):
            dp[0][0][k_th] = 0  # cash
            # dp[0][1][k_th] = -prices[0]  # hold

        for t in range(1, len(prices)):

            for k_th in range(1,k):
                # hold - > 昨天的hold， 今天买入，
                dp[t][1][k_th] = max(dp[t - 1][1][k_th],  # 昨天的hold

                                     dp[t - 1][0][k_th - 1] - prices[t]  # 今天买入: 上一次交易的cash - prices
                                     , - prices[t]
                                     )

                # cash ——> 昨天的cash， 今天卖出
                dp[t][0][k_th] = max(dp[t - 1][0][k_th],  # 昨天的cash

                                     prices[t] + dp[t - 1][1][k_th], 0)  # 今天卖出

                res = max(res, dp[t][0][k_th])
        print(dp)
        return res


k = 2
prices = [3, 3, 5, 0, 0, 3, 1, 4]
solution = Solution()
print(Solution().maxProfit(k, prices))
