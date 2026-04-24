from typing import List


class Solution:
    """
    Runtime
78ms
Beats10.22%
Memory
28.70MB
Beats45.51%
    """

    def maxProfit(self, prices: List[int]) -> int:
        # Base case
        if len(prices)==1:
            return 0

        max_profit = 0
        b = 0
        s = 1

        while b<s and s<=len(prices)-1: 
            buy_price = prices[b]
            sell_price = prices[s]
            
            if sell_price < buy_price:
                # the sell price should be better price to buy
                b = s
            else:
                #  update the max_profit
                max_profit = max(max_profit,sell_price-buy_price)
            s+=1

        return max_profit
        

if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))