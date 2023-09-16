"""
Runtime
Details
61ms
Beats 28.33%of users with Python3
Memory
Details
16.22MB
Beats 60.55%of users with Python3
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x

        while True:
            mid = low + (high-low)//2
            if mid**2 <= x < (mid+1)**2:
                return mid
            elif mid**2 > x:
                high = mid-1
            elif mid**2 < x:
                low = mid+1


if __name__ == "__main__":
    x = 4
    res = Solution().mySqrt(8)
    print(res)
