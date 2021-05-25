# https://leetcode.com/problems/candy/
# Runtime: 152 ms, faster than 91.94% of Python3 online submissions for Candy.
# Memory Usage: 16.9 MB, less than 34.68% of Python3 online submissions for Candy.y.

class Solution:
    def candy(self, ratings) -> int:

        candy_assigned = [1 for _ in range(len(ratings))]

        # 假如当前的小孩比左边的大的话，就在左边的基础上加一:
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candy_assigned[i] = candy_assigned[i - 1] + 1
        # print(candy_assigned)
        # 假如当前的小孩比右边的大的话，就在右边的基础上加一:
        # for i in range(len(ratings) - 1):
        #
        #     if ratings[i] > ratings[i + 1]:
        #         candy_assigned[i] = max(candy_assigned[i], candy_assigned[i + 1] + 1)
        # # print(candy_assigned)
        # return sum(candy_assigned)

        start = len(ratings) - 2
        end = -1

        # 假如当前的小孩比右边的大的话，就在右边的基础上加一, 这是错误的，因为在右边的基础上加一，并不能保证左边也是合法的，所以要最值:

        for i in range(start, end, -1):
            if ratings[i] > ratings[i + 1]:
                candy_assigned[i] = max(candy_assigned[i], candy_assigned[i + 1] + 1)
        # print(candy_assigned)
        return sum(candy_assigned)


if __name__ == "__main__":
    ratings = [1, 3, 4, 5, 2]
    # start = len(ratings) - 2
    # end = -1
    #
    # for i in range(start, end, -1):
    #     print(i)
    print(Solution().candy(ratings))
