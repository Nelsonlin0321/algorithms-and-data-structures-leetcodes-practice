from utils import random_question

# print(random_question()) # 76. Minimum Window Substring.py


# https://leetcode.com/problems/minimum-window-substring/

"""
76. Minimum Window Substring
Hard

6865

461

Add to List

Share
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""

from collections import Counter


class Solution:

    """
    Runtime: 84 ms, faster than 96.44% of Python3 online submissions for Minimum Window Substring.
    Memory Usage: 14.8 MB, less than 86.30% of Python3 online submissions for Minimum Window Substring.
    """

    def minWindow(self, s: str, t: str) -> str:

        if t in s:
            return t

        l_idx = 0
        target_dict = dict(Counter(t))
        window_dict = {}
        target_cnt = len(target_dict)
        window_cnt = 0
        res = ""
        res_length = float("inf")

        for r_idx in range(len(s)):

            right_char = s[r_idx]

            if right_char not in target_dict:
                continue

            if right_char not in window_dict:
                window_dict[right_char] = 1
            else:
                window_dict[right_char] += 1

            if window_dict[right_char] == target_dict[right_char]:
                window_cnt += 1

            # 当窗口已经满足了所有的字符的频率要求后
            while window_cnt == target_cnt:
                left_char = s[l_idx]
                if left_char in target_dict:
                    # 记录结果
                    if target_dict[left_char] == window_dict[left_char]:
                        curr_length = r_idx - l_idx + 1
                        if curr_length < res_length:
                            res_length = r_idx - l_idx + 1
                            res = s[l_idx:r_idx + 1]
                        window_cnt -= 1
                    window_dict[left_char] -= 1
                l_idx += 1

            # while l_idx < len(s) - 1 and s[l_idx] not in target_dict:
            #     l_idx += 1

        return res


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    # s = "a"
    # t = "a"
    print(Solution().minWindow(s, t))
