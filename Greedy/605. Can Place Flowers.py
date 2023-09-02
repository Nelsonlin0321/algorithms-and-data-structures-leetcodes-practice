# https://leetcode.com/problems/can-place-flowers/

from typing import List
"""
Runtime
Details
143ms
Beats 90.99%of users with Python3
Memory
Details
16.82MB
Beats 19.57%of users with Python3
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        i = 0

        num_planted = 0
        num_plot = len(flowerbed)
        while i < num_plot:

            is_planted = flowerbed[i] == 1
            if not is_planted:
                if (i-1 < 0 or flowerbed[i-1] != 1) and (i+1 > num_plot-1 or flowerbed[i+1] != 1):
                    num_planted += 1
                    flowerbed[i] = 1
                    i += 1  # if planted, move one further
            i += 1
        return num_planted >= n


if __name__ == "__main__":
    flowerbed = [1, 0, 0, 0, 1]
    n = 2
    res = Solution().canPlaceFlowers(flowerbed, n)
    print(res)
