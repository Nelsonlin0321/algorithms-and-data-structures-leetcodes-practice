# https://leetcode.com/problems/coin-change/
"""
322. Coin Change
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""
from typing import List


# simple recursive method
# Time Limit Exceeded
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # conquer
        if amount == 0:
            return 0

        if amount in coins:
            return 1

        res_list = []

        # divide
        for coin in coins:

            rest = amount - coin
            if rest >= 0:
                res = self.coinChange(coins, rest)
                if res != -1:  # important
                    res_list.append(1 + res)

        # combine

        if len(res_list) == 0:
            return -1
        else:
            return min(res_list)


"""
Runtime: 1636 ms, faster than 41.92% of Python3 online submissions for Coin Change.
Memory Usage: 14.8 MB, less than 39.56% of Python3 online submissions for Coin Change.
"""


# dynamic program method
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp_dict = {}
        # amount = 0
        dp_dict[0] = 0

        for amt in range(1, amount + 1):
            res_list = []
            for coin in coins:
                res = amt - coin
                if res == 0:
                    res_list.append(1)
                elif res > 0:
                    if res in dp_dict and dp_dict[res] != -1:  # important
                        res_list.append(dp_dict[res] + 1)

            if len(res_list) == 0:
                dp_dict[amt] = -1
            else:
                dp_dict[amt] = min(res_list)

        return dp_dict[amount]



if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    # coins = [2]
    # amount = 3

    print(Solution().coinChange(coins, amount))
    # print(float("inf")>0)
