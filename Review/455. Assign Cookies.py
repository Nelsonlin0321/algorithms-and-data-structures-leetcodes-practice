from typing import List

from utils import random_question


# print(random_question()) 455. Assign Cookies.py


class Solution:

    """
    Runtime: 224 ms, faster than 18.10% of Python3 online submissions for Assign Cookies.
    Memory Usage: 16.1 MB, less than 7.12% of Python3 online submissions for Assign Cookies.
    """

    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g = sorted(g)
        s = sorted(s)

        g_idx = 0
        s_idx = 0

        content = 0
        # stop iteration when we try to assign all cookie
        while 0 <= s_idx <= len(s) - 1 and 0 <= g_idx <= len(g) - 1 :
            if g[g_idx] <= s[s_idx]:
                g_idx += 1
                s_idx += 1
                content += 1
            else:
                s_idx += 1

        return content


if __name__ == "__main__":
    g = [1, 2, 3]
    s = [1, 1]

    print(Solution().findContentChildren(g,s))
