class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        
        res = 0
        need = 0
        
        for i in range(len(s)):
            char = s[i]
            
            if char == '(':
                need+=1
            else:
                need-=1
            
            if need==-1:
                res+=1
                need=0
        
        return res+need