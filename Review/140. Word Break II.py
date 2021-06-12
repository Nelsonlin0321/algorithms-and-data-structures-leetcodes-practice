from typing import List

from utils import random_question

# print(random_question())
# 140. Word Break II.py

"""
140. Word Break II
Hard

3293

446

Add to List

Share
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
"""


class Solution:
    """
    Runtime: 28 ms, faster than 82.43% of Python3 online submissions for Word Break II.
    Memory Usage: 14.2 MB, less than 65.40% of Python3 online submissions for Word Break II.
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # base case
        if len(s) == 0:
            return []

        res = []
        if s in wordDict:
            res.append(s)

        # divide
        for idx in range(1, len(s)):
            left_str = s[:idx]

            right_str = s[idx:]

            if left_str in wordDict:
                right_res = self.wordBreak(right_str, wordDict)
                # combine
                for right_sub_str in right_res:
                    res.append(" ".join([left_str, right_sub_str]))

        return res


if __name__ == "__main__":
    # s = "pineapplepenapple"
    # wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    # print(Solution().wordBreak(s, wordDict))
    print(list(range(1, 2)))
