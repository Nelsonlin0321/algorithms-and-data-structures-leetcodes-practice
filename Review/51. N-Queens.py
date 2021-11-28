from typing import List
from copy import deepcopy

class Solution:
    def __init__(self):
        self.res = []

    def is_valid(self, board, row, col):

        # the row is fixed, check the col is valid or not

        n = len(board)

        # we select the col, same row checking
        for row_id in range(n):
            if board[row_id][col] == 'Q':
                return False

        # we select the row, same col checking
        for col_id in range(n):
            if board[row][col_id] == 'Q':
                return False

        # left upper dig checking
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == 'Q':
                return False

        # right upper checking
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i][j] == 'Q':
                return False

        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        row = ['.' for _ in range(n)]
        board = [deepcopy(row) for _ in range(n)]
        self.backtracking(board,0)
        return self.res

    def backtracking(self, board, row):

        if row == len(board):
            self.res.append(["".join(row) for row in board])
            return

        # we select the row, and check  under this row, which col we can select
        for col in range(len(board)):
            if not self.is_valid(board, row, col):
                continue
            board[row][col] = 'Q'
            self.backtracking(board, row + 1)
            board[row][col] = '.'


