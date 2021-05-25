# https://leetcode.com/problems/assign-cookies/
# Runtime: 164 ms, faster than 40.91% of Python3 online submissions for Assign Cookies.
# Memory Usage: 15.9 MB, less than 64.23% of Python3 online submissions for Assign Cookies.

class Solution:
    def findContentChildren(self, g, s) -> int:
        g_idx = 0
        g.sort()  # 胃口
        s_idx = 0
        s.sort()  # 饼干

        n_child = 0
        if g[0] > s[-1]:  # 最小的胃口，用最大的饼干都喂不满足的话
            return n_child

        while 0 <= g_idx <= len(g) - 1 and 0 <= s_idx <= len(s) - 1:
            if s[s_idx] >= g[g_idx]:
                s_idx += 1
                g_idx += 1
                n_child += 1

            elif s[s_idx] < g[g_idx]:
                # 说明当前的饼干不能满足该小孩， 饼干要再大一点
                s_idx += 1

        return n_child


if __name__ == "__main__":
    g = [10, 9, 8, 7]
    s = [5, 6, 7, 8]
    print(Solution().findContentChildren(g, s))
