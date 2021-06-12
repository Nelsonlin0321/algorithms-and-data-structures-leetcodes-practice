from typing import List

from utils import random_question

# print(random_question())

# 241. Different Ways to Add Parentheses.py
# https://leetcode.com/problems/different-ways-to-add-parentheses/
"""
241. Different Ways to Add Parentheses
Medium

2251

120

Add to List

Share
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
"""


class Solution:
    def calculate(self, left_num, right_num, oper):
        if oper == '+':
            return left_num + right_num
        elif oper == '*':
            return left_num * right_num
        elif oper == '-':
            return left_num - right_num

    def diffWaysToCompute(self, expression: str) -> List[int]:

        # conquer # the smallest problem
        if expression.isdigit():
            return [int(expression)]

        res = []
        # divide
        for idx in range(len(expression)):
            if expression[idx] in "+-*":
                opr = expression[idx]
                left_expr = expression[:idx]
                right_expr = expression[idx + 1:]

                # how to combine ?
                left_res = self.diffWaysToCompute(left_expr)
                right_res = self.diffWaysToCompute(right_expr)

                for left_num in left_res:
                    for right_num in right_res:
                        res.append(self.calculate(left_num, right_num, opr))
        return res

# Runtime: 36 ms, faster than 66.81% of Python3 online submissions for Different Ways to Add Parentheses.
# Memory Usage: 14.4 MB, less than 50.00% of Python3 online submissions for Different Ways to Add Parentheses.

if __name__ == "__main__":
    expression = "2*3-4*5"
    print(Solution().diffWaysToCompute(expression))
