from typing import List


# recursive solution
# Time Limit Exceeded
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # base case
        if amount == 0:
            return 0

        coins_change_list = []

        for coin in coins:
            if coin <= amount:
                next_change = self.coinChange(coins, amount - coin)
                if next_change != -1:
                    coins_change_list.append(next_change + 1)
        if len(coins_change_list) == 0:
            return -1

        return min(coins_change_list)


# BFS
# Time Limit Exceeded
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0
        return self.BFS(coins, amount)

    def BFS(self, coins, amount):

        change_cnt = 1

        coins.sort(reverse=True)

        queue = [amount - coin for coin in coins if coin <= amount]

        while len(queue) != 0:

            size = len(queue)

            for idx in range(size):
                next_amount = queue[idx]
                if next_amount == 0:
                    return change_cnt
                # breath function
                next_amount_list = [next_amount - coin for coin in coins if coin <= next_amount]
                if 0 in next_amount_list:
                    return change_cnt + 1

                if len(next_amount_list) != 0:
                    queue.extend(next_amount_list)
            change_cnt += 1
            queue = queue[size:]

        return -1


# DynamicPrograming
# Runtime: 1904 ms, faster than 19.20% of Python3 online submissions for Coin Change.
# Memory Usage: 19.1 MB, less than 16.36% of Python3 online submissions for Coin Change.
class Solution:

    def __init__(self):
        self.largest_amount = None

    def coinChange(self, coins: List[int], amount: int) -> int:

        self.largest_amount = amount + 1
        dp_dict = {}

        if amount == 0:
            return 0

        # base case
        dp_dict[0] = 0
        for coin in coins:
            dp_dict[coin] = 1

        if amount not in dp_dict:
            dp_dict[amount] = self.helper(dp_dict, coins, amount)

        return dp_dict[amount]

    def helper(self, dp_dict, coins, amount):

        # conquer
        if amount in dp_dict:
            return dp_dict[amount]
        if amount < 0:
            return -1

        res = float('inf')

        # divide
        for coin in coins:
            subprolem = self.helper(dp_dict, coins, amount - coin)
            if subprolem == -1:
                continue
            # combine
            res = min(res, subprolem + 1)

        dp_dict[amount] = res if res != float('inf') else -1

        return dp_dict[amount]


if __name__ == "__main__":
    coins = [2]
    amount = 3

    coins = [186, 419, 83, 408]
    amount = 6249
    # coins = [1, 2, 5]
    # amount = 11
    print(Solution().coinChange(coins, amount))
