from typing import List

"""
Runtime
Details
138ms
Beats 87.23%of users with Python3
Memory
Details
19.14MB
Beats 91.99%of users with Python3
"""


class Solution:
    def candy(self, ratings: List[int]) -> int:

        num_rating = len(ratings)
        assignments = [1 for _ in range(num_rating)]

        # from left to right
        for i in range(1, num_rating):
            left = ratings[i-1]
            right = ratings[i]
            if right > left:
                if assignments[i] <= assignments[i-1]:
                    assignments[i] = assignments[i-1]+1

        # from right to left
        for i in range(num_rating-1, 0, -1):
            right = ratings[i]
            left = ratings[i-1]
            if left > right:
                if assignments[i-1] <= assignments[i]:
                    assignments[i-1] = assignments[i]+1

        return sum(assignments)


if __name__ == "__main__":
    ratings = [1, 3, 4, 5, 2]
    res = Solution().candy(ratings=ratings)
    print(res)
