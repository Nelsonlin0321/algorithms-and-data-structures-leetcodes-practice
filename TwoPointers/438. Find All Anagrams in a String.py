from collections import Counter

# Runtime: 96 ms, faster than 97.33% of Python3 online submissions for Find All Anagrams in a String.
# Memory Usage: 15.3 MB, less than 35.76% of Python3 online submissions for Find All Anagrams in a String.
# 细节很重要
class Solution(object):

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        left = 0
        res = []
        target_dict = dict(Counter(p))
        window_dict = {char: 0 for char in p}
        target_cnt = len(target_dict)
        current_cnt = 0
        window_size = len(p)
        for right in range(len(s)):

            right_char = s[right]

            if right_char in target_dict:
                window_dict[right_char] += 1

                if window_dict[right_char] == target_dict[right_char]:
                    current_cnt += 1
                    if current_cnt >= target_cnt:
                        res.append(left)

            while (right - left + 1) >= window_size:

                left_char = s[left]

                if left_char in target_dict:

                    if window_dict[left_char] == target_dict[left_char]:
                        current_cnt -= 1

                    window_dict[left_char] -= 1

                left += 1

        return res


s ="acdcaeccde"
p = "c"

print(Solution().findAnagrams(s, p))
