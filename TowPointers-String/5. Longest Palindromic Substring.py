"""
Success
Details
Runtime: 1392 ms, faster than 53.16% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14 MB, less than 86.73% of Python3 online submissions for Longest Palindromic Substring.
"""


class Solution:

    def get_palindrome(self, s, left, right):

        while 0 <= left <= len(s) - 1 and 0 <= right <= len(s) - 1 and s[left] == s[right]:
            left -= 1
            right += 1

        left += 1
        right -= 1

        return s[left:right + 1]

    def longestPalindrome(self, s: str) -> str:

        longest_palindrome = ""

        for i in range(len(s)):
            palindrome_1 = self.get_palindrome(s, i, i)
            palindrome_2 = self.get_palindrome(s, i, i + 1)

            max_palindrome = palindrome_1 if len(palindrome_1) >= len(palindrome_2) else palindrome_2
            longest_palindrome = max_palindrome if len(max_palindrome) >= len(longest_palindrome) else longest_palindrome

        return longest_palindrome

