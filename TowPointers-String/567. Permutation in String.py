from collections import Counter


# time limit exceeding
class Solution(object):

    def __init__(self):
        self.combs = []

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        used = [False for _ in range(len(s1))]

        self.permutation(s1, used, [])

        self.combs = set(self.combs)

        wid_size = len(s1)
        loop_cnt = len(s2) - wid_size + 1

        for idx in range(len(s2)):
            sub_str = s2[idx:idx + wid_size]
            if sub_str in self.combs:
                return True

        return False

    def permutation(self, s, used, comb):

        if len(comb) == len(s):
            self.combs.append("".join(comb))
            return

        for idx in range(len(s)):
            if not used[idx]:
                comb.append(s[idx])
                used[idx] = True
                self.permutation(s, used, comb)
                comb.pop()
                used[idx] = False


# Runtime: 1496 ms, faster than 20.64% of Python3 online submissions for Permutation in String.
# Memory Usage: 14.3 MB, less than 83.42% of Python3 online submissions for Permutation in String.
class Solution(object):

    def checkInclusion(self, s1, s2):

        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        target_dict = Counter(s1)

        wid_size = len(s1)
        loop_cnt = len(s2) - wid_size + 1

        for idx in range(loop_cnt):
            sub_str = s2[idx:idx + wid_size]
            if Counter(sub_str) == target_dict:
                return True

        return False


# Runtime: 52 ms, faster than 98.40% of Python3 online submissions for Permutation in String.
# Memory Usage: 14.4 MB, less than 60.49% of Python3 online submissions for Permutation in String.

class Solution(object):

    def checkInclusion(self, s1, s2):

        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if len(s2) < len(s1):
            return False

        target_dict = dict(Counter(s1))
        match_dict = dict(Counter(s2[:len(s1)]))

        target_formed = len(target_dict)
        formed = 0

        for char in match_dict:
            if char in target_dict and match_dict[char] >= target_dict[char]:
                formed += 1

        if formed == target_formed:
            return True

        wid_size = len(s1)
        loop_cnt = len(s2) - len(s1) + 1

        for idx in range(1, loop_cnt):

            head = s2[idx + wid_size - 1]

            if head in target_dict:

                if head in match_dict:
                    match_dict[head] += 1
                else:
                    match_dict[head] = 1

                if match_dict[head] >= target_dict[head] > match_dict[head] - 1:
                    formed += 1

            tail = s2[idx - 1]

            if tail in target_dict:

                match_dict[tail] -= 1

                if match_dict[tail] < target_dict[tail] <= match_dict[tail] + 1:
                    formed -= 1

            if formed == target_formed:
                return True

        return False


# Solution 2
# Runtime: 68 ms, faster than 78.44% of Python3 online submissions for Permutation in String.
# Memory Usage: 14.4 MB, less than 60.58% of Python3 online submissions for Permutation in String.

class Solution(object):

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        left = 0
        wid_size = len(s1)
        target_dict = dict(Counter(s1))
        window_dict = {char: 0 for char in s1}
        target_cnt = len(target_dict)
        current_cnt = 0

        for right in range(len(s2)):
            # 右指针向右边移动

            right_char = s2[right]
            # 只有当 right_char 在 match_dict 中才更新
            if right_char in window_dict:
                window_dict[right_char] += 1

                if window_dict[right_char] == target_dict[right_char]:
                    current_cnt += 1

            # 判断是否已经满足要求了
            if current_cnt >= target_cnt:
                return True

            # 判断是否满足一个这个字符要求
            # 左边指针移动判断: 当窗口的长度大于等于 指针 窗口长度
            while (right - left + 1) >= wid_size:

                left_char = s2[left]

                if left_char in window_dict:

                    if window_dict[left_char] == target_dict[left_char]:
                        current_cnt -= 1

                    window_dict[left_char] -= 1

                left += 1

        return False


s1 = "adc"
s2 = "dcda"

# s1 = "ab"
# s2 = "eidboaoo"
print(Solution().checkInclusion(s1, s2))

# str_1 = "abc"
# str_2 = "bca"
# print(Counter(str_1) == Counter(str_2))
