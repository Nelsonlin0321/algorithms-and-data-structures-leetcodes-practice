class Solution:
    def isValid(self, s: str) -> bool:
        
        count_dict = {'(':0,'[':0,'{':0}
        right_to_left_dict = {')':'(',
                              ']':'[',
                              '}':'{'}
        
        left_chars = []
        for i in range(len(s)):
            char = s[i]
            
            # if char is the left symbol
            if char in count_dict:
                count_dict[char]+=1
                left_chars.append(char)
                
            # if char is the right symbol
            else:
                if not left_chars:
                    return False
                
                left_char = left_chars.pop(-1)
                left_char_ = right_to_left_dict[char]
                
                if left_char==left_char_:
                    count_dict[left_char]-=1

                if count_dict[left_char]==-1:
                    return False
        
        return sum(count_dict.values())==0