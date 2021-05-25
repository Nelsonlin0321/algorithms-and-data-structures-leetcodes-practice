# Runtime: 56 ms, faster than 88.88% of Python3 online submissions for Best Time to Buy and Sell Stock II.
# Memory Usage: 15.2 MB, less than 19.85% of Python3 online submissions for Best Time to Buy and Sell Stock II.

class Solution:
    def maxProfit(self, prices) -> int:

        max_profit = 0
        for t in range(1, len(prices)):
            if prices[t] > prices[t - 1]:
                max_profit = max_profit + (prices[t] - prices[t - 1])

        return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]

    print(Solution().maxProfit(prices))
