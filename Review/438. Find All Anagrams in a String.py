from typing import List

from utils import random_question

# print(random_question()) # 438. Find All Anagrams in a String.py

from collections import Counter


class Solution:
    """
    Runtime: 116 ms, faster than 80.18% of Python3 online submissions for Find All Anagrams in a String.
    Memory Usage: 15.3 MB, less than 36.72% of Python3 online submissions for Find All Anagrams in a String.
    """

    def findAnagrams(self, s: str, p: str) -> List[int]:

        target_dict = Counter(p)
        target_cnt = len(target_dict)

        # window_dict = {}
        window_dict = {char: 0 for char in p}

        window_cnt = 0

        left = 0

        res = []
        for right in range(len(s)):
            right_char = s[right]

            if right_char not in target_dict:
                continue

            # right update: 右边字典更新 + 1
            window_dict[right_char] += 1

            # record：右边满足结果记录 +1
            if window_dict[right_char] == target_dict[right_char]:
                window_cnt += 1

            # 左边收缩条件判断：当 right left 的字符差 len(p), left 需要收缩值 len(p)
            while (right + 1 - left) > len(p):

                left_char = s[left]
                if left_char in target_dict:
                    if window_dict[left_char] == target_dict[left_char]:
                        # record: 左边满足结果记录 -1
                        window_cnt -= 1

                    # update: 左边字典更新 -1
                    window_dict[left_char] -= 1

                left += 1

            # 跳出循环： 就是(right + 1 - left) == len(p):添加结果
            if window_cnt == target_cnt:
                res.append(left)

        return res


if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    print(Solution().findAnagrams(s, p))
