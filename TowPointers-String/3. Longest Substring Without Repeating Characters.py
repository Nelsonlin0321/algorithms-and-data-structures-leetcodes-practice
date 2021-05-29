# Time Limit Exceeded
# 986 / 987 test cases passed.
class Solution(object):

    def is_duplicates(self, sub_str):

        return len(sub_str) != len(set(sub_str))

    def lengthOfLongestSubstring(self, s):

        """
        :type s: str
        :rtype: int
        """
        # all_str = s
        # base case
        if len(s) <= 1:
            return len(s)

        # left = 0
        # right = len(all_str)
        res = 1
        for left in range(len(s)):

            for right in range(
                    len(s),
                    left,
                    -1):
                sub_string = s[left:right];
                if not self.is_duplicates(sub_string):
                    res = max(len(sub_string), res)
                    break
        return res


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        temp = s[0]
        max_len = 1
        for letter in s[1:]:
            if letter in temp:
                i = temp.find(letter)
                temp = temp[i + 1:]
            temp += letter
            if len(temp) > max_len:
                max_len = len(temp)
        return max_len


"""
indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d
          ^                  ^
          |                  |
		left               right
		seen = {a : 0, c : 1, b : 2, d: 3} 
		# case 1: seen[b] = 2, current window  is s[0:4] , 
		#        b is inside current window, seen[b] = 2 > left = 0. Move left pointer to seen[b] + 1 = 3
		seen = {a : 0, c : 1, b : 4, d: 3} 
indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d
						 ^   ^
					     |   |
				      left  right		
indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d
					     ^       ^
					     |       |
				       left    right		
		# case 2: seen[a] = 0,which means a not in current window s[3:5] , since seen[a] = 0 < left = 3 
		# we can keep moving right pointer.
"""


# Runtime: 52 ms, faster than 90.51% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.4 MB, less than 53.47% of Python3 online submissions for Longest Substring Without Repeating Characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        output = 0
        for r in range(len(s)):
            """
            If s[r] not in seen, we can keep increasing the window size by moving right pointer
            """
            if s[r] not in seen:
                output = max(output, r - l + 1)

            else:  # 当该元素是已经见过了

                if seen[s[r]] >= l:  # 如果这个见过的元素，包含在区间里。我们需要在左边的区间把他剔除掉
                    l = seen[s[r]] + 1
                else:
                    output = max(output, r - l + 1)  # 如果这个见过的元素，不在包含的区间里， 我们就只需要计算新的长度
            # 更新最近见过的元素的索引
            seen[s[r]] = r

        return output


if __name__ == "__main__":
    # print(list(range(5,3,-1)))
    s = "abcabcbb"
    # print(Solution().lengthOfLongestSubstring(s))

    print("abc".find("a"))
