from collections import Counter

"""
Runtime: 1552 ms, faster than 19.99% of Python3 online submissions for Permutation in String.
Memory Usage: 14.2 MB, less than 86.57% of Python3 online submissions for Permutation in String.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # base case
        if len(s2) < len(s1):
            return False

        if s1 in s2:
            return True

        target_dict = dict(Counter(s1))

        window_size = len(s1)

        slot_num = len(s2) - window_size + 1

        for start_idx in range(slot_num):
            sub_string = s2[start_idx:start_idx + window_size]
            sub_dict = dict(Counter(sub_string))
            if sub_dict == target_dict:
                return True
        return False

"""
Runtime: 67 ms, faster than 79.61% of Python3 online submissions for Permutation in String.
Memory Usage: 14.5 MB, less than 8.93% of Python3 online submissions for Permutation in String.
"""
class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        # base case
        if len(s2) < len(s1):
            return False

        if s1 in s2:
            return True

        left = 0
        target_dict = dict(Counter(s1))
        curr_dict = {}

        target_num = len(target_dict)
        curr_num = 0

        for right in range(len(s2)):
            right_char = s2[right]
            if right_char in target_dict:
                """右边字典更新+1"""
                if right_char in curr_dict:
                    curr_dict[right_char] += 1
                else:
                    curr_dict[right_char] = 1
                """右边满足条件+1"""
                if curr_dict[right_char] == target_dict[right_char]:
                    curr_num += 1

            """左边收缩条件判断： while"""
            while (right - left) > len(s1)-1: ### left 0 right 2 -> three chars!!!
                left_char = s2[left]
                if left_char in target_dict:
                    """左边满足结果记录 -1"""
                    if curr_dict[left_char] == target_dict[left_char]:
                        curr_num -= 1
                    """左边字典更新 -1"""
                    curr_dict[left_char] -= 1
                left += 1
            """满足条件返回"""
            if curr_num == target_num:
                return True

        return False


if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    print(Solution().checkInclusion(s1, s2))
