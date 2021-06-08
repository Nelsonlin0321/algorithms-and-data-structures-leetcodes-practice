from typing import List


# Runtime: 108 ms, faster than 5.10% of Python3 online submissions for Best Time to Buy and Sell Stock II.
# Memory Usage: 15.1 MB, less than 20.73% of Python3 online submissions for Best Time to Buy and Sell Stock II.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for t in range(len(prices) - 1):
            if prices[t + 1] > prices[t]:
                max_profit = max_profit + (prices[t + 1] - prices[t])

        return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))
