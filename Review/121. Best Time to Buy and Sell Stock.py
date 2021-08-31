from typing import List


class Solution:
    """
    Runtime: 1292 ms, faster than 13.01% of Python3 online submissions for Best Time to Buy and Sell Stock.
    Memory Usage: 25.9 MB, less than 11.57% of Python3 online submissions for Best Time to Buy and Sell Stock.
    """
    def maxProfit(self, prices: List[int]) -> int:
        # base case
        if len(prices) <= 1:
            return 0

        # two status
        hold = [None for _ in range(len(prices))]
        unhold = [None for _ in range(len(prices))]

        # base case
        hold[0] = -prices[0]
        unhold[0] = 0

        for indx in range(1, len(prices)):
            # hold
            hold[indx] = max(-prices[indx], hold[indx-1])

            # sell or
            sell = hold[indx - 1] + prices[indx]

            unhold[indx] = max(sell, unhold[indx - 1])

        return unhold[-1]

if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))