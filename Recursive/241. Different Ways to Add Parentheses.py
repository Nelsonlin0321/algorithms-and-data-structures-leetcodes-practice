from typing import List
# https://leetcode.com/problems/different-ways-to-add-parentheses/submissions/
# Success
# Details
# Runtime: 40 ms, faster than 41.04% of Python3 online submissions for Different Ways to Add Parentheses.
# Memory Usage: 14.1 MB, less than 99.75% of Python3 online submissions for Different Ways to Add Parentheses.

class Solution:
    def helper(self, oper, num_1, num_2):
        if oper == '-':
            return num_1 - num_2
        if oper == "+":
            return num_1 + num_2
        if oper == "*":
            return num_1 * num_2

    def diffWaysToCompute(self, expression: str) -> List[int]:
        # conquer
        if expression.isdigit():
            return [int(expression)]
        else:
            res = []
            for (idx, char) in enumerate(expression):
                if char in "-+*":
                    # divide
                    res_1 = self.diffWaysToCompute(expression[:idx])  # left
                    res_2 = self.diffWaysToCompute(expression[idx + 1:])  # right

                    # combine
                    for num_1 in res_1:
                        for num_2 in res_2:
                            res.append(self.helper(
                                expression[idx],
                                num_1,
                                num_2
                            ))
            return res


if __name__ == "__main__":
    expression = "2*3-4*5"
    print(Solution().diffWaysToCompute(expression))

