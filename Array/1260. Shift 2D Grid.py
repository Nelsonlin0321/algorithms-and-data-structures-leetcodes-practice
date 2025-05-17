from typing import List
"""
Accepted
107 / 107 testcases passed
Nelson Lin
Nelson Lin
submitted at May 17, 2025 13:50
Runtime
4ms
Beats73.45%
Analyze Complexity
Memory
18.12MB
Beats73.70%
"""

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        n_row = len(grid)
        m_col = len(grid[0])

        nums = []
        for i in range(n_row):
            for j in range(m_col):
                nums.append(grid[i][j])
        
        size = len(nums)
        
        k = k%size
        nums_shift = nums[-k:]+nums[:size-k]
        
        z = 0 
        for i in range(n_row):
            for j in range(m_col):
                grid[i][j] = nums_shift[z]
                z+=1

        return grid