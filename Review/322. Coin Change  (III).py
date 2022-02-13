"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

"""
from typing import List


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        "base case"

        if amount == 0:
            return 0

        if len(coins) == 0:
            return -1

        sub_res_list = []
        for coin in coins:
            if coin <= amount:
                remain = amount - coin
                sub_res = self.coinChange(coins, remain)
                if sub_res != -1:
                    sub_res += 1

                sub_res_list.append(sub_res)

        if len(sub_res_list) == 0:
            return -1
        else:
            return min(sub_res_list)


"""
Runtime: 1125 ms, faster than 93.00% of Python3 online submissions for Coin Change.
Memory Usage: 14.2 MB, less than 83.72% of Python3 online submissions for Coin Change.
"""

class Solution:

    def __init__(self):
        self.dp = []

    def coinChange(self, coins: List[int], amount: int) -> int:

        self.dp = [-1 for _ in range(amount + 1)]
        self.dp[0] = 0

        for amt in range(1, amount + 1):  # 状态 - 子问题
            # # 状态转移方程
            self.dp[amt] = self.transit_func(amt, coins)

        return self.dp[-1]

    def transit_func(self, amt, coins):
        # 状态转移方程
        res = -1
        for coin in coins:
            if coin <= amt:
                remain = amt - coin
                if self.dp[remain] != -1:
                    if res != -1:
                        res = self.dp[remain] + 1 if self.dp[remain] + 1 < res else res
                    else:
                        res = self.dp[remain] + 1
        # 选择
        return res


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11

    print(Solution().coinChange(coins, amount))
