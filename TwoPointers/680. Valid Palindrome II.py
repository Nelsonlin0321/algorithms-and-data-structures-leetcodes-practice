"""
Runtime
Details
110ms
Beats 72.52%of users with Python3
Memory
Details
16.90MB
Beats 38.71%of users with Python3
"""


class Solution:

    def isPalindrome(self, s):
        return s == s[::-1]

    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1

        while i <= j:
            left = s[i]
            right = s[j]

            if left != right:
                left_is_palindrome = self.isPalindrome(s[i:j])  # remove right
                right_is_palindrome = self.isPalindrome(
                    s[i+1:j+1])  # remove left
                return left_is_palindrome or right_is_palindrome

            i += 1
            j -= 1

        return True


if __name__ == "__main__":
    s = "abc"
    res = Solution().validPalindrome(s)
    print(res)
