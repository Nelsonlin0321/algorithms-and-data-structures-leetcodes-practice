# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#
#         left = 0
#         right = 0
#         visited_dict = {char: False for char in s}
#         longest_length = 0
#         unique_flag = True
#
#         while right < len(s):
#             right_char = s[right]
#
#             # if already visited
#             if visited_dict[right_char]:
#                 unique_flag = False
#                 length = right - left
#                 longest_length = length if length > longest_length else longest_length
#                 left_char = s[left]
#                 left += 1
#                 visited_dict[left_char] = False
#
#             else:
#                 length = right - left + 1
#                 longest_length = length if length > longest_length else longest_length
#
#             visited_dict[right_char] = True
#
#             right += 1
#
#         if unique_flag:
#             return len(s)
#
#         return longest_length


"""
Runtime: 185 ms, faster than 21.99% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.1 MB, less than 70.69% of Python3 online submissions for Longest Substring Without Repeating Characters.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_length = 0
        visited_dict = {char: 0 for char in s}

        while right < len(s):
            right_char = s[right]
            visited_dict[right_char] += 1

            while visited_dict[right_char] > 1: # 难点：当有重复的时候就要收缩left 指针

                # 更新left 指针
                left_char = s[left]
                visited_dict[left_char] -= 1
                left += 1

            # until no duplicate
            print(s[left:right+1])
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length


if __name__ == "__main__":
    # s = "abcabcbb"
    s = "aab"
    s = "pwwkew"
    # s = "bbbb"
    # s = "dvdf"
    print(Solution().lengthOfLongestSubstring(s))
