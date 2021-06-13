from typing import List


class Solution:
    """
    Runtime: 44 ms, faster than 41.28% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
    Memory Usage: 14.9 MB, less than 14.26% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
    """

    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0

        hold = [-float("inf") for _ in prices]
        cash = [-float("inf") for _ in prices]

        hold[0] = -prices[0]
        cash[0] = 0

        hold[1] = max(hold[0], -prices[1])
        cash[1] = max(cash[0], hold[1] + prices[1])

        for t in range(2, len(prices)):
            hold[t] = max(hold[t - 1], cash[t - 2] - prices[t])  # 1) 不变， 2）买入, 因为买入这一时刻，上一时刻不能卖出，cash[t-1]不合法
            cash[t] = max(cash[t - 1], hold[t] + prices[t])

        return cash[-1]


prices = [1, 2, 3, 0, 2]

print(Solution().maxProfit(prices))
