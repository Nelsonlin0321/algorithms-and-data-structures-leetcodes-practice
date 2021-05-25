import sys
from collections import Counter


# Time Limit Exceeded
# class Solution:
#     def helper(self, sub_str, t):
#         counter_t = Counter(t)
#         counter_sub_str = Counter(sub_str)
#
#         for (key, value) in counter_t.items():
#             if counter_t[key] > counter_sub_str[key]:
#                 return False
#         return True
#
#     def minWindow(self, s: str, t: str) -> str:
#
#         str_set = set([char for char in s])
#
#         # 直接判断t 是否就在s 中
#         if t in s:
#             return t
#
#         window_size = len(t)
#
#         while (window_size <= len(s)):
#             for idx in range(len(s) - window_size + 1):
#                 sub_str = s[idx:idx + window_size]
#                 is_match = self.helper(sub_str, t)
#                 if is_match:
#                     return sub_str
#             window_size += 1
#         return ""
# def is_included(string, sub_string):
#     if len(string) < len(sub_string):
#         return False
#     else:
#         sub_str_counter = Counter(sub_string)
#         string_counter = Counter(string)
#         for (char, cnt) in sub_str_counter.items():
#             if string_counter[char] < sub_str_counter[char]:
#                 return False
#         return True

## Time Limit Exceeded
# class Solution:
#
#     def is_included(self, string, sub_string):
#         if len(string) < len(sub_string):
#             return False
#         else:
#             sub_str_counter = Counter(sub_string)
#             string_counter = Counter(string)
#             for (char, cnt) in sub_str_counter.items():
#                 if string_counter[char] < sub_str_counter[char]:
#                     return False
#             return True
#
#     def minWindow(self, s: str, t: str) -> str:
#
#         target_dict = dict(Counter(t))
#
#         if t in s:
#             return t
#
#         head = 1
#         max_tail = 0
#         min_str = s
#         is_found = False
#
#         while head <= len(s):
#
#             for tail_idx in range(max_tail, head):
#                 string = s[tail_idx:head]
#                 if self.is_included(string, t):
#                     is_found = True
#                     if len(string) < len(min_str):
#                         min_str = string
#                     max_tail_idx = max(max_tail_idx, tail_idx)
#                 else:
#                     break
#             head += 1
#
#         if not is_found:
#             return ""
#         else:
#             return min_str

# Time Limit Exceeded
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_dict = dict(Counter(t))  # """ {A:1,B:1,C:1}"""
        formed = 0
        slow = 0
        min_str = None
        min_length = sys.maxsize - 1

        for fast in range(len(s)):
            """
            skip if s[fast] doesn't master
            """
            char = s[fast]
            fast += 1
            if char not in target_dict:
                continue
            """
            记录目前为止fast 的指针是否 包含了 target_str的所有字符了
            """
            # fast_str = s[:fast]
            target_dict[char] -= 1
            if target_dict[char] == 0:
                formed += 1

            while formed == len(target_dict) and slow <= fast:
                curr_length = fast - slow
                if curr_length < min_length:
                    min_length = curr_length
                    min_str = s[slow:fast]
                """
                一旦满足了条件后，试图尝试把左边的指针，缩小。
                 update the left boundary
                """
                char = s[slow]
                slow += 1
                if char not in target_dict:
                    continue
                # 当我们移除的字符在 tareg_dict里面的话，
                target_dict[char] += 1  # target +=1 说明这个字符还需要再匹配，还欠这个字符的债
                if target_dict[char] == 1:  # 我们欠这个字符
                    formed -= 1

        return min_str if min_str is not None else ""


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().minWindow(s, t))
