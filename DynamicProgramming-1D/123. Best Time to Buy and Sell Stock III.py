from typing import List


#
# Runtime: 1744 ms, faster than 12.93% of Python3 online submissions for Best Time to Buy and Sell Stock III.
# Memory Usage: 36.2 MB, less than 11.62% of Python3 online submissions for Best Time to Buy and Sell Stock III.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        # base case the first day
        # 定义 第一阶段持有与卖出的最佳收益
        hold_1 = [-float('inf') for _ in range(len(prices))]
        hold_1[0] = - prices[0]

        cash_1 = [-float('inf') for _ in range(len(prices))]
        cash_1[0] = 0

        # 定义 第二阶段持有与卖出的最佳收益
        hold_2 = [-float('inf') for _ in range(len(prices))]
        # hold_1[0] = - prices[0]

        cash_2 = [-float('inf') for _ in range(len(prices))]
        # cash_1[0] = 0

        for t in range(1, len(prices)):
            # t
            hold_1[t] = max(hold_1[t - 1], -prices[t])
            cash_1[t] = max(cash_1[t - 1], prices[t] + hold_1[t - 1])

            # if cash_1[t-1]!=
            hold_2[t] = max(hold_2[t - 1], cash_1[t - 1] - prices[t])
            cash_2[t] = max(cash_2[t - 1], prices[t] + hold_2[t - 1], cash_1[t])
            max_profit = max(max_profit, cash_2[t])

        return max_profit


prices = [1, 2, 3, 4, 5]

print(Solution().maxProfit(prices))
