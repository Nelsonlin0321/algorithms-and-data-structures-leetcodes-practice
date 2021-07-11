from typing import List


# recursive method
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # base case # conquer

        if amount == 0:
            return 0

        if min(coins) > amount:
            return -1

        if amount in coins:
            return 1

        # divide
        res_list = []
        for coin in coins:
            if coin <= amount:
                remain = amount - coin
                sub_res = self.coinChange(coins, remain)
                if sub_res != -1:
                    res_list.append(sub_res + 1)

        if len(res_list) == 0:
            return -1

        # combine
        return min(res_list)

"""
Runtime: 1728 ms, faster than 31.36% of Python3 online submissions for Coin Change.
Memory Usage: 19.4 MB, less than 15.07% of Python3 online submissions for Coin Change.
"""


# dynamic programing
# top to bottom
class Solution:

    def __init__(self):
        """is a dict because the status is not consequential"""
        self.dp_dict = {}

    def coinChange(self, coins: List[int], amount: int) -> int:

        # base case # conquer
        if amount == 0:
            self.dp_dict[amount] = 0
            return self.dp_dict[amount]

        if min(coins) > amount:
            self.dp_dict[amount] = -1
            return self.dp_dict[amount]

        if amount in coins:
            self.dp_dict[amount] = 1
            return self.dp_dict[amount]

        # divide
        res_list = []
        for coin in coins:
            if coin <= amount:
                remain = amount - coin
                """check if it's in dp dictionary"""
                if remain in self.dp_dict:
                    sub_res = self.dp_dict[remain]
                else:
                    sub_res = self.coinChange(coins, remain)
                if sub_res != -1:
                    res_list.append(sub_res + 1)

        # combine
        if len(res_list) == 0:
            self.dp_dict[amount] = -1
            return self.dp_dict[amount]
        else:
            self.dp_dict[amount] = min(res_list)
            return self.dp_dict[amount]


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    print(Solution().coinChange(coins, amount))
