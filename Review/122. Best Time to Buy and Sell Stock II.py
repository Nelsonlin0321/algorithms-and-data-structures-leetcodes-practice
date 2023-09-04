from typing import List
"""
Runtime
Details
69ms
Beats 51.46%of users with Python3
Memory
Details
17.84MB
Beats 20.52%of users with Python3
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        i = 0
        max_profit = 0

        while i < len(prices):
            buy_price = prices[i]
            if i+1 < len(prices):
                sell_price = prices[i+1]
                profit = sell_price - buy_price
                if profit > 0:
                    max_profit += profit
                i += 1
            else:
                break

        return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    res = Solution().maxProfit(prices)
    print(res)
