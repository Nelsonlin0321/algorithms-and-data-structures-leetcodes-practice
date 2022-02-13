import math
"""
Success
Details 
Runtime: 820 ms, faster than 71.42% of Python3 online submissions for Perfect Squares.
Memory Usage: 34.6 MB, less than 8.34% of Python3 online submissions for Perfect Squares.
"""
class Solution:

    def get_breath(self, n):

        max_num = int(math.sqrt(n))

        for sqr in range(max_num, 0, -1):
            yield n - sqr ** 2

    def numSquares(self, n: int) -> int:

        queue = [n]
        num_sqr = 0

        while len(queue) != 0:
            size = len(queue)
            for idx in range(size):
                curr_num = queue[idx]
                # 判断时候到达终点
                if curr_num == 0:
                    return num_sqr

                # 广度搜索函数
                for sqr in self.get_breath(curr_num):
                    if sqr == 0:
                        return num_sqr + 1
                    queue.append(sqr)

            num_sqr += 1
            queue = queue[size:]


if __name__ == "__main__":
    n = 12
    print(Solution().numSquares(
        n
    ))
