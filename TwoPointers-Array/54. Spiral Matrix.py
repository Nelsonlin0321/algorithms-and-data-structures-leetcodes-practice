from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        
        upper_bound = 0
        lower_bound  = m
        
        left_bound = 0
        right_bound = n
        
        res =[]
        count = 0
        while count<m*n:
            
            if count < m*n:
                # ->
                for i in range(left_bound,right_bound):
                    res.append(matrix[upper_bound][i])
                    count+=1
                upper_bound+=1
            
            if count < m*n:
                #|
                #v
                for i  in range(upper_bound,lower_bound):
                    res.append(matrix[i][right_bound-1])
                    count+=1
                right_bound-=1
            
            if count < m*n:
                # <-
                for i in range(right_bound-1,left_bound-1,-1):
                    res.append(matrix[lower_bound-1][i])
                    count+=1

                lower_bound-=1
            
            if count < m*n:
                # ^
                # |
                for i in range(lower_bound-1,upper_bound-1,-1):
                    # print(i)
                    # print(left_bound)
                    # print('='*10)
                    res.append(matrix[i][left_bound])
                    count+=1

                left_bound+=1
        
        return res

class Solution:
    def spiralOrder(self , matrix ):
        
        output_matrix = []

        while (len(matrix)!=0 and len(matrix[0])!=0):
            #获取第一行
            if len(matrix)!=0 and len(matrix[0])!=0:
                output_matrix.extend(matrix[0])
                matrix =  matrix[1:] # 剔除第一行
            else:
                break

            if len(matrix)!=0 and len(matrix[0])!=0:
                # 获取最后一列
                output_matrix.extend([row[-1] for row in matrix])
                # 剔除最后一列
                matrix = [row[:-1] for row in matrix if len(row)!=0]
            else:
                break

            if len(matrix)!=0 and len(matrix[0])!=0:
                # 获取最后一行 # 倒遍历
                output_matrix.extend(matrix[-1][::-1]) 
                matrix =  matrix[:-1] # 剔除最后一行
            else:
                break

            if len(matrix)!=0 and len(matrix[0])!=0:
                output_matrix.extend([row[0] for row in matrix[::-1] if len(row)!=0])
                # 剔除最后一列
                matrix = [row[1:] for row in matrix]
            else:
                break
        return output_matrix

if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(Solution().spiralOrder(matrix))
    
        
        
            
            
                
    
                
            
        