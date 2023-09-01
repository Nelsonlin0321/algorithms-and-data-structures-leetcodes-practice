# https://leetcode.com/problems/coin-change/

"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""

"""
Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0


"""


class Solution(object):

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        dp = [0] + [float("inf")]*amount

        # loop for each status
        for amt in range(1, amount+1):

            # selection
            for coin in coins:
                if coin <= amt:
                    # transition
                    dp[amt] = min(dp[amt], dp[amt-coin]+1)

        return -1 if dp[amount] == float("inf") else dp[amount]


if __name__ == "__main__":
    coins = [2]
    amount = 3
    res = Solution().coinChange(coins=coins, amount=11)
    print(res)
