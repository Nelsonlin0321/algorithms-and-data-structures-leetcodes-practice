from copy import deepcopy


# Runtime: 144 ms, faster than 21.84% of Python3 online submissions for N-Queens.
# Memory Usage: 14.9 MB, less than 11.15% of Python3 online submissions for N-Queens.

class Solution:

    def isValid(self, board, row, col):

        n = len(board)
        for i in range(len(board)):
            if board[i][col] == 'Q':
                return False

        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i][j] == 'Q':
                return False

        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == 'Q':
                return False

        return True

    def __init__(self):
        self.res = []

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        row = ["." for _ in range(n)]
        board = [deepcopy(row) for _ in range(n)]
        self.backtrack(board, 0)
        return self.res

    def backtrack(self, board, row):

        if row == len(board):
            self.res.append(["".join(row) for row in board])
            return

        for col in range(len(board)):
            if not self.isValid(board, row, col):
                continue

            board[row][col] = 'Q'
            self.backtrack(board, row + 1)
            board[row][col] = '.'


if __name__ == "__main__":
    n = 4
    solution = Solution()
    res = solution.solveNQueens(4)
    print(res)
    # print(len(set(["".join(item) for item in res])))

    # path = [1,2,3,4]
    # print()
    # de_path = deepcopy(path)
    # # print(de_path)
