class Solution:

    def __init__(self):
        self.dp_dict = {}

    def wordBreak(self, string, wordDict):

        # base case
        if len(string) == 0:
            return True

        if string in set(wordDict):
            self.dp_dict[string] = True
            return True

        if string in set(self.dp_dict):
            return self.dp_dict[string]

        for idx in range(1, len(string)):

            left_str = string[:idx]

            right_str = string[idx:]

            if left_str in set(wordDict) and self.wordBreak(right_str, wordDict):
                self.dp_dict[string] = True
                return self.dp_dict[string]

        self.dp_dict[string] = False

        return self.dp_dict[string]


s = "aaaaaaaaaaaaaaaaaaaaaaaabaaaaa"
wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
solution = Solution()
res = solution.wordBreak(s, wordDict)
print(solution.dp_dict)
