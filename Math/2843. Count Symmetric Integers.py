"""
Runtime
Details
903ms
Beats 18.89%of users with Python3
Memory
Details
16.32MB
Beats 44.55%of users with Python3
"""


def is_symmetric(number):
    str_number = str(number)
    if len(str_number) % 2 == 1:
        return False

    i = len(str_number) // 2

    left_str = str_number[0:i]
    left_sum = sum([int(n) for n in left_str])
    right_str = str_number[i:]
    right_sum = sum([int(n) for n in right_str])

    return left_sum == right_sum


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for n in range(low, high+1):
            if is_symmetric(n):
                count += 1

        return count


if __name__ == "__main__":
    res = Solution().countSymmetricIntegers(low=1200, high=1230)
    print(res)
