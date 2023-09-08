"""
Runtime
Details
319ms
Beats 32.50%of users with Python3
Memory
Details
16.31MB
Beats 37.07%of users with Python3
"""


class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        left = 0
        right = int(c**(1/2))  # upper limit

        while left <= right:
            sqr_sum = left**2+right**2

            if sqr_sum == c:
                return True

            if sqr_sum > c:
                right -= 1
            elif sqr_sum < c:
                left += 1

        return False


if __name__ == "__main__":
    import time
    c = 100000000
    start = time.time()
    res = Solution().judgeSquareSum(c)
    end = time.time()
    spent = round((end-start)*1000, 2)
    print(res)
    print(f"Spent:{spent} ms")
