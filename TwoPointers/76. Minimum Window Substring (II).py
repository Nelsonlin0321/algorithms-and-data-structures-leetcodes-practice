"""
Runtime: 107 ms, faster than 83.13% of Python3 online submissions for Minimum Window Substring.
Memory Usage: 14.8 MB, less than 74.28% of Python3 online submissions for Minimum Window
"""

class Solution:

    def minWindow(self, s: str, t: str) -> str:

        # base case

        if t in s:
            return t

        left = 0
        right = 0

        target_dict = {}

        target_num = len(set(t))

        curr_num = 0
        min_window = ""
        min_length = float("inf")

        for char in t:
            if char not in target_dict:
                target_dict[char] = 1
            else:
                target_dict[char] += 1

        record_dict = {char: 0 for (char, freq) in target_dict.items()}

        while right < len(s):

            right_char = s[right]

            if right_char in target_dict:
                # right 指针的更新操作
                if record_dict[right_char] - target_dict[right_char] == -1:
                    curr_num += 1

                record_dict[right_char] += 1

            # left 只针对额缩小操作

            while left < right + 1 and curr_num == target_num:
                # 细节： right + 1 , 因为字符索引要加一，索引起点为零
                min_window = s[left:right + 1] if (right - left + 1) < min_length else min_window
                min_length = right - left + 1 if (right - left + 1) < min_length else min_length

                left_char = s[left]
                # left 指针的操作
                if left_char in target_dict:
                    # 细节： 判断 left 指针会不会 影响到 curr_num 满足 字符串的个数
                    if record_dict[left_char] == target_dict[left_char]: # 假如在没有 减一之前是相等的，就会令满足的字符串个数少一
                        curr_num -= 1

                    # 只要在 记录的字典里，左字符都要减一
                    record_dict[left_char] -= 1

                left += 1

            # 当 left 判断完后 right + 1
            right += 1

        return min_window


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    # s = 'ab'
    # t = 'a'
    # s = 'ab'
    # t = 'b'
    s = "acbbaca"
    t = "aba"
    print(Solution().minWindow(s, t))
