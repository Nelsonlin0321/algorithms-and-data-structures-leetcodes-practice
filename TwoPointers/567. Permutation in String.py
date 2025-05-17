import collections
"""
https://leetcode.com/problems/permutation-in-string/submissions/1636281006/
Accepted
108 / 108 testcases passed
Nelson Lin
Nelson Lin
submitted at May 17, 2025 18:15
Runtime
19ms
Beats67.54%
Analyze Complexity
Memory
18.05MB
Beats18.80%
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        win_size = len(s1)
        
        if len(s2)<win_size:
            return False
        
        left = 0 
        right = 0
        
        window_dict,need_dict = {},{}
        valid_n  = 0
        
        for c in s1:
            need_dict[c] = need_dict.get(c,0)+1
        
        required_n = len(need_dict)
        
        while right < len(s2):

            c = s2[right]
            if c in need_dict:
                window_dict[c] = window_dict.get(c,0)+1
                if window_dict[c]==need_dict[c]:
                    valid_n+=1
            
            while right-left+1>=win_size:
                if valid_n == required_n:
                    return True
                
                c = s2[left]
                left+=1

                if c in need_dict:
                    if window_dict[c]==need_dict[c]:
                        valid_n-=1
                    window_dict[c]-=1

            right+=1

        return False

class Solution:
    # 判断 s 中是否存在 t 的排列
    def checkInclusion(self, t: str, s: str) -> bool:
        need, window = collections.defaultdict(int), collections.defaultdict(int)
        for c in t: 
            need[c] += 1

        left, right, valid = 0, 0, 0 
        while right < len(s):
            c = s[right]
            right += 1
            # 进行窗口内数据的一系列更新
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            # 判断左侧窗口是否要收缩
            while (right - left >= len(t)):
                # 在这里判断是否找到了合法的子串
                if valid == len(need):
                    return True
                d = s[left]
                left += 1
                # 进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        # 未找到符合条件的子串
        return False
    
class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        win_size = len(s1)
        #  base case
        if len(s2)<win_size:
            return False
        
        left = 0 
        right = 0
        
        window_dict = {}
        need_dict = {}

        for c in s1:
            need_dict[c] = need_dict.get(c,0)+1
        
        while right < len(s2):

            c = s2[right]
            window_dict[c] = window_dict.get(c,0)+1
            
        
            while right-left+1==win_size:
                
                #  chec the window dict is same as need_dict
                all_equal = True

                for c in need_dict:
                    if c not in window_dict or need_dict[c]!= window_dict[c]:
                        all_equal = False
                        break
                
                if all_equal:
                    return True
                
                c = s2[left]
                window_dict[c] = window_dict[c]-1

                left+=1
            
            right+=1
        
        return False
    


    def checkInclusion(self, s1: str, s2: str) -> bool:
        win_size = len(s1)
        
        if len(s2)<win_size:
            return False
        
        left = 0 
        right = 0
        
        window_dict,need_dict = {},{}
        
        valid_n  = 0
        required_n = 0

        for c in s1:
            need_dict[c] = need_dict.get(c,0)+1
        
        while right < len(s2):
            c = s2[right]
            if c in need_dict:
                window_dict[c] = window_dict.get(c,0)+1
                if window_dict[c]==need_dict:
                    valid_n+=1
            
            while right-left+1>=win_size:
                if valid_n == required_n:
                    return True
                
                c = s2[left]
                left+=1

                if c in need_dict:
                    if window_dict[c]==need_dict[c]:
                        valid_n-=1
                    window_dict[c]-=1
            right+=1

        return False