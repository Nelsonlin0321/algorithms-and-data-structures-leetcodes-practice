# https://leetcode.com/problems/spiral-matrix-ii/

"""
Success
Details 
Runtime: 36 ms, faster than 88.14% of Python3 online submissions for Spiral Matrix II.
Memory Usage: 13.9 MB, less than 82.31% of Python3 online submissions for Spiral Matrix II.
"""

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        row = [None for _ in range(n)]
        matrix = [row.copy() for _ in range(n)]
        
        upper=0
        lower=n-1
        
        left=0
        right =n-1
        
        count = 1
        while  count <= n*n:
            
            if count <= n*n:
                # upper
                for i in range(left,right+1):
                    matrix[upper][i] = count
                    count+=1
                upper+=1
            
            if count <= n*n:
                # right
                for i in range(upper,lower+1):
                    matrix[i][right]=count
                    count+=1
                right-=1
            
            if count <= n*n:
                # lower
                for i in range(right,left-1,-1):
                    matrix[lower][i] = count
                    count+=1
                lower-=1
            
            if count <= n*n:
                #left
                for i in range(lower,upper-1,-1):
                    matrix[i][left]=count
                    count+=1
                left+=1
        
        return matrix
    

if __name__ == "__main__":
    n = 3
    print(Solution().generateMatrix(n))
            
            
                
                
         
        