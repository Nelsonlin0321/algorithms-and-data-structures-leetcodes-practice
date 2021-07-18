from typing import List


class Solution:
    """
    Runtime: 24 ms, faster than 96.15% of Python3 online submissions for Word Break II.
    Memory Usage: 14.4 MB, less than 9.87% of Python3 online submissions for Word Break II.
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # base case

        res = []

        if len(wordDict) == 0:
            return []

        # conquer
        if s in wordDict:
            res.append(s)

        # divide
        for idx in range(1, len(s)):
            left_str = s[:idx]
            right_str = s[idx:]
            if left_str in wordDict:
                right_res = self.wordBreak(right_str, wordDict)
                # combine
                for right_sub_res in right_res:
                    sub_res = left_str + " " + right_sub_res
                    res.append(sub_res)

        return res


if __name__ == "__main__":
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    print(Solution().wordBreak(s, wordDict))
