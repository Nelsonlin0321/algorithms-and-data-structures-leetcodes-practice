from typing import List


# Time Limit Exceeded
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for t in range(1, len(prices)):
            #  sell on t th day
            profit = prices[t] - min(prices[:t])
            max_profit = max(max_profit, profit)

        return max_profit

# Runtime: 1356 ms, faster than 8.38% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25.2 MB, less than 51.11% of Python3 online submissions for Best Time to Buy and Sell Stock.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0

        if not prices:
            return max_profit

        min_price = prices[0]

        for t in range(1, len(prices)):
            #  sell on t th day
            min_price = min(prices[t], min_price)
            profit = prices[t] - min_price
            max_profit = max(max_profit, profit)

        return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))
