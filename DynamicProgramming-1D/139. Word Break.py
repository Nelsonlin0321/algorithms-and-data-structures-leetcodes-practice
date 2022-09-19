"""
Submission Detail
42 / 42 test cases passed.
Status: Accepted
Runtime: 72 ms
Memory Usage: 14.5 MB
Submitted: 1 year, 3 months ago
You are here!
Your runtime beats 35.38 % of python3 submissions.
"""
class Solution:

    def __init__(self):
        self.dp_dict = {}

    def wordBreak(self, string, wordDict):

        # base case
        # conquer
        if len(string) == 0:
            return True

        if string in set(wordDict):
            self.dp_dict[string] = True
            return True

        if string in set(self.dp_dict):
            return self.dp_dict[string]

        # divide
        for idx in range(1, len(string)):

            left_str = string[:idx]

            right_str = string[idx:]

            if left_str in set(wordDict) and self.wordBreak(right_str, wordDict):
                self.dp_dict[string] = True
                # combine : any if true return true
                return self.dp_dict[string]

        self.dp_dict[string] = False

        return self.dp_dict[string]


s = "aaaaaaaaaaaaaaaaaaaaaaaabaaaaa"
wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
solution = Solution()
res = solution.wordBreak(s, wordDict)
print(solution.dp_dict)
