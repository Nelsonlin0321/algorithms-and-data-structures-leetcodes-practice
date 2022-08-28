"""
5. Longest Palindromic Substring
Medium

21019

1212

Add to List

Share
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


"""
"""
Time Limit Exceeded
"""

def is_palindromic(sub_str):
    if len(sub_str) == 1:
        return True

    left = 0
    right = len(sub_str)-1

    while left < right:
        if sub_str[left] == sub_str[right]:
            left += 1
            right -= 1
        else:
            return False

    return True


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # base case
        if len(s) <= 1:
            return s

        MAX_LENGTH = 0
        MAX_SUBSTR = ""

        left = 0
        for left in range(len(s)-1):
            right = len(s)
            has_palindromic = False
            while left < right:
                sub_str = s[left:right]
                if is_palindromic(sub_str):
                    if len(sub_str) > MAX_LENGTH:
                        MAX_LENGTH = len(sub_str)
                        MAX_SUBSTR = sub_str
                    has_palindromic = True
                
                if has_palindromic:
                    break
                else:
                    right -= 1

        return MAX_SUBSTR

"""
Submission Detail
140 / 140 test cases passed.
Status: Accepted
Runtime: 1162 ms
Memory Usage: 14.1 MB
"""


class Solution:
    
    def get_palindrome(self,s,left,right):
        
        while 0 <= left <= len(s) - 1 and 0 <= right <= len(s) - 1 and s[left] == s[right]:
            left -= 1
            right +=1
        
        left += 1
        right -=1
        
        return s[left:right+1]
        
    def longestPalindrome(self, s: str) -> str:
        
        max_length = 0
        longest_palindrome = ""
        
        for i in range(len(s)):
            
            palindrom_1 = self.get_palindrome(s,i,i)
            # print(palindrom_1)
            palindrom_2 = self.get_palindrome(s,i,i+1)
            
            
            max_palindrom = palindrom_1 if len(palindrom_1)>=len(palindrom_2) else palindrom_2

            longest_palindrome = max_palindrom if len(max_palindrom)>len(longest_palindrome) else longest_palindrome
                   
        return longest_palindrome



if __name__ == "__main__":
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    print(Solution().longestPalindrome(s=s))
