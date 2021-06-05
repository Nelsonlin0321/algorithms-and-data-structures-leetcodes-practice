# Runtime: 88 ms, faster than 5.72% of Python3 online submissions for Word Break II.
# Memory Usage: 14.1 MB, less than 86.17% of Python3 online submissions for Word Break II.

class Solution:

    def __init__(self):
        self.dp_break_dict = {}

    def wordBreak(self, string, wordDict):

        # base case
        # conquer
        if len(string) == 0:
            return []

        if string in set(self.dp_break_dict):
            return self.dp_break_dict[string]

        res = []

        """
        string = "aa"
        dict = ["a","aa"]
        aa - > a a , aa
        """
        # divide
        if string in set(wordDict):
            res.append(string)

        for idx in range(1, len(string)):

            left_str = string[:idx]

            right_str = string[idx:]

            if right_str not in set(self.dp_break_dict):
                right_break_list = self.wordBreak(right_str, wordDict)
                self.dp_break_dict[right_str] = right_break_list
            else:
                right_break_list = self.dp_break_dict[right_str]

            if left_str in set(wordDict) and len(right_break_list) != 0:
                # combine
                for right_break in right_break_list:
                    break_list = [left_str, right_break]
                    res.append(" ".join(break_list))

        self.dp_break_dict[string] = res

        return res


s = "aaaaaaa"
wordDict = ["aaaa", "aa", "a"]

solution = Solution()
res = solution.wordBreak(s, wordDict)
# print(solution.dp_break_dict)
print(res)
