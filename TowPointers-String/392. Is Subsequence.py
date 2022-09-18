# https://leetcode.com/problems/is-subsequence/

"""
Runtime: 37 ms, faster than 86.81% of Python3 online submissions for Is Subsequence.
Memory Usage: 14 MB, less than 12.84% of Python3 online submissions for Is Subsequence.
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # base case
        if len(s)==0:
            return True
        if len(t)==0:
            return False
        
        i = len(s)-1
        j = len(t)-1
        
        
        while 0<=i<len(s) and 0<=j<len(t):
            
            s_char = s[i]
            t_char = t[j]
            if s_char==t_char:
                i-=1
            j-=1
        
        return i==-1
            
            
        
        