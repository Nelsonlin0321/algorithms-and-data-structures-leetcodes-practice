# https://leetcode.com/problems/coin-change-ii/

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [0 for _ in range(amount+1)]
        dp[0]=1
        
        for coin in coins:
            for amt in range(1,amount+1):
                if amt-coin >=0:
                    dp[amt] = dp[amt] + dp[amt-coin]
        return dp[amount]