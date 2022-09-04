# https://leetcode.com/problems/regular-expression-matching/

"""
当 p[j + 1] 为 * 通配符时，我们分情况讨论下：

1、如果 s[i] == p[j]，那么有两种情况：

1.1 p[j] 有可能会匹配多个字符，比如 s = "aaa", p = "a*"，那么 p[0] 会通过 * 匹配 3 个字符 "a"。

1.2 p[i] 也有可能匹配 0 个字符，比如 s = "aa", p = "a*aa"，由于后面的字符可以匹配 s，所以 p[0] 只能匹配 0 次。

2、如果 s[i] != p[j]，只有一种情况：

p[j] 只能匹配 0 次，然后看下一个字符是否能和 s[i] 匹配。比如说 s = "aa", p = "b*aa"，此时 p[0] 只能匹配 0 次。
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        i = 0
        j = 0
        
        
        while i< len(s) and j < len(p):
            
            # match
            if s[i] == p[j] or p[j]=='.':
                
                if j+1 > len(p) and p[j+1] =="*":
                    # can match 0 for more
                    pass
        pass
    

            
            
    
        