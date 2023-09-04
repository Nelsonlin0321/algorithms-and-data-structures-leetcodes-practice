# https://leetcode.com/problems/queue-reconstruction-by-height/description/
from typing import List
"""
Runtime
Details
94ms
Beats 76.37%of users with Python3
Memory
Details
16.98MB
Beats 67.05%of users with Python3
"""


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:

        # highest first
        people = sorted(people, key=lambda x: x[1])
        people = sorted(people, key=lambda x: x[0], reverse=True)
        # people = sorted(people, key=lambda x: x[1])
        # print(people)
        re_people = [people[0]]

        i = 1
        n_people = len(people)
        while i < n_people:
            person = people[i]
            nth = person[1]  # the number of people ahead of it
            re_people.insert(nth, person)
            i += 1

        return re_people


if __name__ == "__main__":
    people = [[9, 0], [7, 0], [1, 9], [3, 0], [2, 7],
              [5, 3], [6, 0], [3, 4], [6, 2], [5, 2]]
    res = Solution().reconstructQueue(people)
    print(res)
