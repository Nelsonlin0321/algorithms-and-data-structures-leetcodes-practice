# https://leetcode.com/problems/regular-expression-matching/

"""
当 p[j + 1] 为 * 通配符时，我们分情况讨论下：

1、如果 s[i] == p[j]，那么有两种情况：

1.1 p[j] 有可能会匹配多个字符，比如 s = "aaa", p = "a*"，那么 p[0] 会通过 * 匹配 3 个字符 "a"。

1.2 p[i] 也有可能匹配 0 个字符，比如 s = "aa", p = "a*aa"，由于后面的字符可以匹配 s，所以 p[0] 只能匹配 0 次。

2、如果 s[i] != p[j]，只有一种情况：

p[j] 只能匹配 0 次，然后看下一个字符是否能和 s[i] 匹配。比如说 s = "aa", p = "b*aa"，此时 p[0] 只能匹配 0 次。
"""


class Solution:
    # 备忘录
    def __init__(self):
        self.memo = None

    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        self.memo = [[-1 for _ in range(n)] for _ in range(m)]
        # 指针 i，j 从索引 0 开始移动
        return self.dp(s, 0, p, 0)

    # 计算 p[j..] 是否匹配 s[i..]
    def dp(self, s: str, i: int, p: str, j: int) -> bool:
        m, n = len(s), len(p)
        # base case
        if j == n:
            return i == m
        if i == m:
            if (n - j) % 2 == 1:
                return False
            for j in range(j, n, 2):
                if p[j + 1] != '*':
                    return False
            return True

        # 查备忘录，防止重复计算
        if self.memo[i][j] != -1:
            return self.memo[i][j] == 1

        res = False
        if s[i] == p[j] or p[j] == '.':
            if j < n - 1 and p[j + 1] == '*':
                # 匹配 0 次, 或者 匹配 多 次， 忽略当前字符 i
                res = self.dp(s, i, p, j + 2) or self.dp(s, i + 1, p, j)
            else:
                res = self.dp(s, i + 1, p, j + 1)
        else:
            # 不匹配， 且 p[j + 1] 是 *， * 匹配0次， p 跳過當前字符 j 和 j+1 *
            if j < n - 1 and p[j + 1] == '*':
                res = self.dp(s, i, p, j + 2)
            else:
                res = False

        # 将当前结果记入备忘录
        self.memo[i][j] = 1 if res else 0
        return res
