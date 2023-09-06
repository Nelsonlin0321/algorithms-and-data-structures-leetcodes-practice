# https://leetcode.com/problems/reverse-words-in-a-string/submissions/

"""
Success
Details 
Runtime: 72 ms, faster than 17.42% of Python3 online submissions for Reverse Words in a String.
Memory Usage: 14.2 MB, less than 15.80% of Python3 online submissions for Reverse Words in a String.

"""

def reverseString(string):
    
    chars = list(string)
    left = 0
    right = len(string)-1
    
    while left < right:
        chars[left],chars[right] = chars[right],chars[left]
        left+=1
        right-=1
    
    return "".join(chars)
    
class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = " ".join([c for c in s.split(" ") if c])
        
        reversed_string = reverseString(s)
        
        words_list = []
        
        for words in reversed_string.split(" "):
            words_list.append(reverseString(words))
            
        return " ".join(words_list)
                
s = "a good   example"

print(Solution().reverseWords(s))