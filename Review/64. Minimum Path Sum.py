# https://leetcode.com/problems/minimum-path-sum/
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Find relative small problems as examples and solve it natively.   
        During which, define subproblems represented by a db table that can be inferred to solve the problem. 
        Explain: dp[4][3]=4, is one of subproblems, which means the minimum path sum for the grid with the shape (4,3) is 4.
        The problem dp[i][j] can be solved by ``min(val+dp[i-1][j],val+dp[i][j-1]), which is the inferring function```
        """

        num_cols = len(grid[0])
        rows = [float("inf") for _ in range(num_cols)]
        num_rows = len(grid)
        dp = [rows.copy() for _ in range(num_rows)]

        "2) base cases: base cases that are known at the beginning"
        dp[0][0] = grid[0][0]

        """3) Loop for each subproblem """
        for row_i in range(num_rows):
            for col_i in range(num_cols):

                if row_i == 0 and col_i == 0:
                    continue

                """4) An inferring function: solve the sub problem by inferring the previous solved subproblems"""

                val = grid[row_i][col_i]
                if 0 <= row_i-1 < num_rows:
                    dp[row_i][col_i] = min(dp[row_i][col_i],
                                           val+dp[row_i-1][col_i])

                if 0 <= col_i-1 < num_cols:
                    dp[row_i][col_i] = min(dp[row_i][col_i],
                                           val+dp[row_i][col_i-1])

        return dp[-1][-1]


if __name__ == "__main__":
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    res = Solution().minPathSum(grid=grid)
    print(res)
