from typing import List

"""
Runtime
Details
1188ms
Beats 58.11%of users with Python3
Memory
Details
62.78MB
Beats 44.30%of users with Python3
"""


class Solution:

    def get_overlap(self, left, right):
        if right[0] <= left[1]:
            return [right[0], left[1]]
        return []

    def findMinArrowShots(self, points: List[List[int]]) -> int:

        # base case
        num_points = len(points)
        if num_points <= 1:
            return num_points

        points = sorted(points, key=lambda x: x[0])
        points = sorted(points, key=lambda x: x[1])

        left_point = points[0]
        i = 1
        n_arrow = 1

        while i < num_points:
            right_point = points[i]
            left_point = self.get_overlap(left_point, right_point)

            if not left_point:  # not overlapping
                n_arrow += 1
                left_point = right_point

            i += 1

        return n_arrow


if __name__ == "__main__":
    points = [[3, 9], [7, 12], [3, 8], [6, 8], [
        9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]]
    res = Solution().findMinArrowShots(points)
    print(res)
