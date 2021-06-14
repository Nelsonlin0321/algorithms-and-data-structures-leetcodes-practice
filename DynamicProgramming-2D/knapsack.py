from typing import List

"""
question:
给你一个背包，能够装下N物品，载重为4，
给定有重量和价值的物品，求出该背包可以携带的最大价值

N = 3
W = 4

wt = [2,1,3]
val = [4,2,3]

res = 6


"""


class Solution:

    def knapsack(self, N: int, W: int, wt: List[int], val: List[int]) -> int:
        # base case

        W_ = [None for _ in range(W + 1)]
        dp = [W_.copy() for _ in range(N + 1)]

        # base case
        # dp[N][W] ->
        for n in range(N + 1):
            dp[n][0] = 0
        for w in range(W + 1):
            dp[0][w] = 0

        for n in range(1, N + 1):  # 物品
            for w in range(1, W + 1):

                weight = wt[n - 1]

                if weight > w:
                    # 该物品质量比背包的载重还大， 选择不装
                    dp[n][w] = dp[n - 1][w]

                else:
                    dp[n][w] = max(
                        dp[n - 1][w - weight] + val[n - 1],  # 装
                        dp[n - 1][w]
                    )

        return dp[-1][-1]

N = 3
W = 4
wt = [2, 1, 3]
val = [4, 2, 3]

print(Solution().knapsack(N, W, wt, val))
