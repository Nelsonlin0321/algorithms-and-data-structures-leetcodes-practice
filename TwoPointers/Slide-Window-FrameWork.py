from collections import Counter


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        # base case
        if t in s:
            return t

        # Optional
        # 记录变量，例如匹配到的个数
        res = s
        is_found = False
        valid_size = 0

        # 步骤一: 我们需要判断滑动窗是否涵盖了所有字符,创建当前与目标的状态变量
        window_char_dict = {char: 0 for char in t}  # 记录滑动窗口
        target_char_dict = dict(Counter(t))  # 记录目标

        # 步骤二:逐渐移动右指针
        left = 0
        for right in range(len(s)):

            # 步骤二、获取右指针的字符 并相应更新
            right_char = s[right]
            if right_char not in target_char_dict:
                continue

            # 步骤三：右指针相应更新 --> 更新移动窗口的字典
            window_char_dict[right_char] += 1
            # 判断是否满足当前的字符串： 该字符的频数大于等于目标字典，但是-1 不符合，说明满足了一个字符串的要求
            if window_char_dict[right_char] >= target_char_dict[right_char] > window_char_dict[right_char] - 1:
                valid_size += 1

            # 步骤四：判断目前的移动窗口是否满足要求  -> 满足要求的话， 左边就要收缩
            while valid_size == len(target_char_dict):

                # 步骤五： 记录状态

                # 移动窗口满足要求的话，left 指针要尽可能向右边移动,移动到不符合目标字符串停止
                is_found = True
                # 满足的话： 更新最小字符串
                window_string = s[left:right + 1]
                if len(window_string) <= len(res):
                    res = window_string

                # 步骤六： 移动左指针，将其从滑动窗口中剔除，并且相应更新
                # 将左边的字符移除窗口
                # 并且更新窗口字符串计数
                left_char = s[left]
                if left_char in target_char_dict:
                    window_char_dict[left_char] -= 1
                    if window_char_dict[left_char] < target_char_dict[left_char]:
                        valid_size -= 1
                left += 1

        return res if is_found else ""
