# https://leetcode.com/problems/koko-eating-bananas/description/

"""
Accepted
126 / 126 testcases passed
Nelson Lin
Nelson Lin
submitted at May 19, 2025 22:28
Runtime
184ms
Beats22.90%
Analyze Complexity
Memory
18.78MB
Beats92.77%

"""


from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # speed
        left = 1
        right = 10**9

        while left <= right:
            mid = left+(right-left)//2
            hours = self.get_hours(piles, mid)

            if hours > h:
                #  which means eat slower, need to increase the speed
                left = mid+1

            if hours < h:
                #  which means eat faster, need to decrease the speed
                right = mid-1

            if hours == h:
                #  slower the speed, check the hour spent is the same ? if not, which mean the reach the slowest limit
                if mid == 1 or self.get_hours(piles, mid-1) != h:
                    return mid

                right = mid-1

        return left

    def get_hours(self, piles: List[int], speed: int):

        hours = 0

        for pile in piles:
            hours += pile//speed

            if pile % speed != 0:
                hours += 1

        return hours


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Speed
        left = 1
        right = 10**9+1

        while left < right:

            #  speed
            mid = left + (right-left) // 2
            hours = self.get_hours(piles, mid)

            if hours > h:
                #  The hour spent larger the target, should increase the speed:
                left = mid+1

            if hours < h:
                #  The hour spent smaller the target, should decrease the speed:
                right = mid

            if hours == h:
                # the hours meets the target
                #  let try slower the speed:
                right = mid

        return left

    def get_hours(self, piles: List[int], speed: int):

        hours = 0

        for pile in piles:
            hours += pile//speed

            if pile % speed != 0:
                hours += 1

        return hours
