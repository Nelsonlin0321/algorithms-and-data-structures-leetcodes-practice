class Solution:
    def minInsertions(self, s: str) -> int:
        
        # the right parenthesis we need
        need  = 0
        
        # how many left parentheses we insert into
        res = 0
        
        for char in s:
            if char == "(":
                # 一个左括号都需要两个右括号
                need+=2
                
                if need % 2 == 1:
                    res+=1
                    need-=1
            
            if char == ")":
				# 我们对右括号需求减少一个
                need-=1
								
				# 如果右括号还不够的话
                if need == -1:
                    # 需要插入一个左括号
                    res+=1
                    
                    # 同时右括号维持一个需求
                    need=1
        
        return need+ res