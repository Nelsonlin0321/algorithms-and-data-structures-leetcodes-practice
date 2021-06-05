# recursive solution
# class Solution:
#     def wordBreak(self, string, wordDict):
#         # base case
#         if len(string) == 0:
#             return True
#
#         if string in wordDict:
#             return True
#
#         for idx in range(1, len(string)):
#
#             left_str = string[:idx]
#
#             right_str = string[idx:]
#
#             if self.wordBreak(left_str, wordDict) and self.wordBreak(right_str, wordDict):
#                 return True
#
#         return False


class Solution:

    def __init__(self):
        self.dp_dict = {}

    def wordBreak(self, string, wordDict):

        # base case
        if len(string) == 0:
            return True

        if string in wordDict:
            return True

        for idx in range(1, len(string)):

            left_str = string[:idx]

            right_str = string[idx:]

            if left_str not in set(self.dp_dict):
                self.dp_dict[left_str] = self.wordBreak(left_str, wordDict)

            if right_str not in set(self.dp_dict):
                self.dp_dict[right_str] = self.wordBreak(right_str, wordDict)

            if self.dp_dict[left_str] and self.dp_dict[right_str]:
                return True

        return False


s = "applepenapple"
wordDict = ["apple", "pen"]

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]

print(Solution().wordBreak(s, wordDict))
