"""
322. Coin Change
Medium

13520

305

Add to List

Share
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

"""


"""
Success
Details 
Runtime: 2351 ms, faster than 47.77% of Python3 online submissions for Coin Change.
Memory Usage: 14.9 MB, less than 31.76% of Python3 online submissions for Coin Change.
"""



from typing import List


class Solution:
    def __init__(self) -> None:
        self.dp_dict = {}
        self.dp_dict[0] =0
        
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        for amt in range(1,amount+1):
            self.dp_dict[amt] = float('inf')
            
            for coin in coins:
                if amt == coin:
                    self.dp_dict[amt]=1
                elif amt > coin:
                    rest = amt-coin
                    self.dp_dict[amt] = min(self.dp_dict[rest]+1,self.dp_dict[amt])
        
        if self.dp_dict[amount]==float('inf'):
            return -1
        
        return self.dp_dict[amount]

if __name__ == "__main__":
    coins = [2]
    amount = 3
    
    print(Solution().coinChange(coins,amount))
        



                    
            
        
        
        
    
    
        