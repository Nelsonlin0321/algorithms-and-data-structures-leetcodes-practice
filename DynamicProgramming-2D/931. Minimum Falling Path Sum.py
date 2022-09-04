# https://leetcode.com/problems/minimum-falling-path-sum/
from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        row = [None for _ in range(n)]
        dp = [row.copy() for _ in range(n)]
        
        # definition
        #dp[i][j]: the distance from i,j to top
        
        # base case
        dp[0] = matrix[0]
        
        for row in range(1,n):
            for col in range(n):
                
                # (row + 1, col - 1)
                left_val = float('inf')
                if 0<=row - 1<n and 0<=col + 1<n:
                    left_val = dp[row - 1][col + 1]
                
                
                # (row + 1, col)
                right_val = float('inf')
                if 0<=row-1<n:
                    down_val = dp[row - 1][col]
                
                
                # (row + 1, col + 1)
                right_val = float('inf')
                if 0<=row - 1<n and 0<=col - 1<n:
                    right_val  = dp[row - 1][col - 1]
                
                dp[row][col] = min([left_val,down_val,right_val])+ + matrix[row][col]
                
        return min(dp[-1])
        
        