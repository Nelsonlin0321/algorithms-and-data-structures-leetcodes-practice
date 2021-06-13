from typing import List


class Solution:
    """
    Runtime: 896 ms, faster than 22.29% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
    Memory Usage: 21.2 MB, less than 77.79% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
    """

    def maxProfit(self, prices: List[int], fee: int) -> int:

        if len(prices) <= 1:
            return 0

        hold = [-float("inf") for _ in prices]
        cash = [-float("inf") for _ in prices]

        hold[0] = -prices[0]
        cash[0] = 0

        for t in range(1, len(prices)):
            hold[t] = max(hold[t - 1], cash[t - 1] - prices[t])
            cash[t] = max(cash[t - 1], hold[t] + prices[t] - fee)

        return cash[-1]

prices = [1,3,2,8,4,9]

fee = 2

print(Solution().maxProfit(prices,fee))

