"""
Runtime: 107 ms, faster than 83.13% of Python3 online submissions for Minimum Window Substring.
Memory Usage: 14.8 MB, less than 74.28% of Python3 online submissions for Minimum Window
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # base case
        if len(t)>len(s):
            return ""
        
        #  char count dict of t string
        t_char_dict = {}
        for c in t:
            t_char_dict[c] = t_char_dict.get(c,0)+1
        
        window_char_dict = {}
        t_char_num = len(t_char_dict)
        valid_n=0

        left = 0
        right = 0

        res = ""
        sub_str_len = float("inf")
        while right < len(s):
            c = s[right]
            if c in t_char_dict:
                window_char_dict[c] = window_char_dict.get(c,0)+1
                if window_char_dict[c]==t_char_dict[c]:
                    #  valid+=1
                    valid_n+=1
            
            # shrink the window
            while valid_n==t_char_num and left<=right:
                #  update the res
                len_ = right-left+1
                if len_ <= sub_str_len:
                    res = s[left:right+1]
                    sub_str_len = len_

                # update the valid dict
                c = s[left]
                if c in t_char_dict:
                    if window_char_dict[c]==t_char_dict[c]:
                        valid_n-=1
                    window_char_dict[c] = window_char_dict[c]-1
                
                left+=1

            right+=1

        return res
if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    # s = 'ab'
    # t = 'a'
    # s = 'ab'
    # t = 'b'
    s = "acbbaca"
    t = "aba"
    print(Solution().minWindow(s, t))
