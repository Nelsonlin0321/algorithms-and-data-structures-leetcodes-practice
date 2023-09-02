from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        num_children = len(g)
        num_cookie = len(s)

        s_i = 0
        g_i = 0

        num_content_children = 0

        while 0 <= g_i < num_children and 0 <= s_i < num_cookie:
            if s[s_i] >= g[g_i]:
                g_i += 1
                s_i += 1
                num_content_children += 1
            else:
                s_i += 1  # continue to find the bigger cookie

        return num_content_children


if __name__ == "__main__":
    g = [1, 2, 3]
    s = [1, 1]
    res = Solution().findContentChildren(g, s)
    print(res)
