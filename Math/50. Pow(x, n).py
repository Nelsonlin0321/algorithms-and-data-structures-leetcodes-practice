"""
Runtime
Details
33ms
Beats 93.57%of users with Python3
Memory
Details
16.04MB
Beats 99.78%of users with Python3
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:

        pow_num = 1

        if n == 0:
            return pow_num

        pos_n = abs(n)

        pow_num = x**n

        return pow_num


if __name__ == "__main__":
    x = 2.0
    n = -2
    res = Solution().myPow(x, n)
    print(res)
