"""
https://leetcode.com/problems/fibonacci-number/submissions/

509. Fibonacci Number
Easy

4913

287

Add to List

Share
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
"""

"""
Runtime: 50 ms, faster than 56.99% of Python3 online submissions for Fibonacci Number.
Memory Usage: 13.9 MB, less than 9.62% of Python3 online submissions for Fibonacci Number.
"""

class Solution:
    def fib(self, n: int) -> int:
        
        if n==0:
            return 0
        
        
        dp = [None for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[-1]
    
"""
Success
Details 
Runtime: 59 ms, faster than 39.07% of Python3 online submissions for Fibonacci Number.
Memory Usage: 13.7 MB, less than 95.72% of Python3 online submissions for Fibonacci Number.
"""

class Solution:
    def fib(self, n: int) -> int:

        if n==0:
            return 0 
        
        cur  = 1
        prev = 0
        
        
        for i in range(2,n+1):
            cur_tmp = cur + prev
            prev = cur
            cur = cur_tmp
        
        return cur
    
    

if __name__ == "__main__":
    pass  
            
        
        
        