import sys
from collections import Counter


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


# Runtime: 388 ms, faster than 15.45% of Python3 online submissions for Minimum Window Substring.
# Memory Usage: 15 MB, less than 12.07% of Python3 online submissions for Minimum Window Substring.

class Solution:

    def window_contain(self, window_char_dict, target_char_dict):

        for char in target_char_dict:
            if window_char_dict[char] < target_char_dict[char]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        # base case
        if t in s:
            return t

        res = s
        is_found = False
        # 我们需要判断滑动窗是否涵盖了所有字符
        window_char_dict = {char: 0 for char in t}
        target_char_dict = dict(Counter(t))

        # 左开右闭
        left, right = 0, 0

        # 逐渐移动右指针
        for right in range(len(s)):
            # 当右指针判断遇到目标字符的时候：
            right_char = s[right]
            if right_char not in target_char_dict:
                continue
            # 更新移动窗口的字典
            window_char_dict[right_char] += 1

            # 判断 目前的移动窗口是否满足要求  -> 满足要求的话， 左边就要收缩
            while self.window_contain(window_char_dict, target_char_dict):
                # 移动窗口满足要求的话，left 指针要尽可能向右边移动,移动到不符合目标字符串停止
                is_found = True

                # 满足的话： 更新最小字符串
                window_string = s[left:right + 1]
                if len(window_string) <= len(res):
                    res = window_string

                # 将左边的字符移除窗口
                # 并且更新窗口字符串计数
                left_char = s[left]
                if left_char in target_char_dict:
                    window_char_dict[left_char] -= 1
                left += 1
        return res if is_found else ""

# Runtime: 124 ms, faster than 41.29% of Python3 online submissions for Minimum Window Substring.
# Memory Usage: 14.9 MB, less than 27.91% of Python3 online submissions for Minimum Window Substring.

class Solution:

    def minWindow(self, s: str, t: str) -> str:
        # base case
        if t in s:
            return t

        res = s
        is_found = False
        valid_size = 0
        # 我们需要判断滑动窗是否涵盖了所有字符
        window_char_dict = {char: 0 for char in t}
        target_char_dict = dict(Counter(t))

        # 左开右闭
        left, right = 0, 0

        # 逐渐移动右指针
        for right in range(len(s)):
            # 当右指针判断遇到目标字符的时候：
            right_char = s[right]
            if right_char not in target_char_dict:
                continue
            # 更新移动窗口的字典
            window_char_dict[right_char] += 1
            # 判断是否满足当前的字符串： 该字符的频数大于等于目标字典，但是-1 不符合，说明满足了一个字符串的要求
            if window_char_dict[right_char] >= target_char_dict[right_char] > window_char_dict[right_char] - 1:
                valid_size += 1

            # 判断 目前的移动窗口是否满足要求  -> 满足要求的话， 左边就要收缩
            while valid_size == len(target_char_dict):
                # 移动窗口满足要求的话，left 指针要尽可能向右边移动,移动到不符合目标字符串停止
                is_found = True

                # 满足的话： 更新最小字符串
                window_string = s[left:right + 1]
                if len(window_string) <= len(res):
                    res = window_string

                # 将左边的字符移除窗口
                # 并且更新窗口字符串计数
                left_char = s[left]
                if left_char in target_char_dict:
                    window_char_dict[left_char] -= 1
                    if window_char_dict[left_char] < target_char_dict[left_char]:
                        valid_size -= 1

                left += 1
        return res if is_found else ""
    
if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().minWindow(s, t))
