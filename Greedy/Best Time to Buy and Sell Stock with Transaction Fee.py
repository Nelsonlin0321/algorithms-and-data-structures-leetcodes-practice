from typing import List
import sys


# class Solution:
#
#     def maxProfit(self, prices: List[int], fee: int) -> int:
#
#         hold = [None for _ in range(len(prices))]
#         hold[0] = -prices[0]
#         unhold = [None for _ in range(len(prices))]
#         unhold[0] = 0
#
#         for t in range(1, len(prices)):
#             hold[t] = max(hold[t - 1], unhold[t - 1] - prices[t])  # 持有股票的状态： 维持持有股票的状态， 或者买入股票， 那么就得花钱买
#
#             sell_profit = prices[t] + hold[t] - fee
#             unhold[t] = max(unhold[t - 1], sell_profit)
#         return unhold[-1]

# Runtime: 680 ms, faster than 78.82% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
# Memory Usage: 21.1 MB, less than 91.26% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.

class Solution:

    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = - prices[0]
        cash = 0
        for t in range(1, len(prices)):
            hold = max(hold, cash - prices[t])  # 持有股票的状态： 维持持有股票的状态， 或者买入股票， 那么就得花钱买

            sell_profit = prices[t] + hold - fee
            cash = max(cash, sell_profit)
        return cash


if __name__ == "__main__":
    prices = [1, 3, 7, 5, 10, 3]
    profit = Solution().maxProfit(prices, 3)
    print(profit)
    # print(-sys.maxsize)
