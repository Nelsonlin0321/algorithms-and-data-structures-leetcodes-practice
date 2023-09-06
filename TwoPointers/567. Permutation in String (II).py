"""
Success
Details
Runtime: 72 ms, faster than 87.41% of Python3 online submissions for Permutation in String.
Memory Usage: 13.9 MB, less than 82.76% of Python3 online submissions for Permutation in String.

"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # base case
        if len(s1) > len(s2):
            return False

        window_size = len(s1)

        target_dict = {}

        for char in s1:
            if char in target_dict:
                target_dict[char] += 1
            else:
                target_dict[char] = 1

        target_num = len(target_dict)

        curr_dict = {char: 0 for (char, num) in target_dict.items()}

        curr_num = 0

        left = 0
        right = 0

        while right < len(s2):
            right_char = s2[right]
            # 判断
            if right_char in target_dict:
                curr_dict[right_char] += 1
                # 细节：假如加一以后满足了次数，那么该满足的字符串个数 + 1
                if curr_dict[right_char] == target_dict[right_char]:
                    curr_num += 1

            while right + 1 - left == window_size:

                if curr_num == target_num:
                    return True

                left_char = s2[left]

                if left_char in target_dict:
                    # 假如在减少之前，字符次数是相等，那么满足字符串的个数 - 1
                    if curr_dict[left_char] == target_dict[left_char]:
                        curr_num -= 1
                    curr_dict[left_char] -= 1

                left += 1

            right += 1

        return False








