# https://leetcode.com/problems/minimum-window-substring/submissions/
"""
Runtime
Details
216ms
Beats 24.24%of users with Python3
Memory
Details
17.12MB
Beats 59.54%of users with Python3
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # base case

        if len(t) > len(s):
            return ""

        s_len = len(s)
        left = 0
        right = 0
        target_dict = {}
        curr_dict = {}

        for char in t:
            if char in target_dict:
                target_dict[char] += 1
            else:
                target_dict[char] = 1
                curr_dict[char] = 0

        target_num = len(target_dict)
        curr_num = 0
        mini_window = None

        while left < s_len and right < s_len:
            window = s[left:right+1]
            right_char = s[right]

            if right_char in target_dict:
                curr_dict[right_char] += 1
                if curr_dict[right_char] == target_dict[right_char]:
                    curr_num += 1

            # check if fullfil
            while curr_num >= target_num:
                has = True
                # check the length
                window = s[left:right+1]
                mini_window = window if mini_window is None or len(
                    window) < len(mini_window) else mini_window

                # shorten the length
                left_char = s[left]
                if left_char in target_dict:
                    if curr_dict[left_char] == target_dict[left_char]:
                        curr_num -= 1
                    curr_dict[left_char] -= 1
                left += 1

            right += 1

        return mini_window if mini_window else ""


if __name__ == "__main__":
    s = "a"
    t = "b"
    res = Solution().minWindow(s, t)
    print(res)
