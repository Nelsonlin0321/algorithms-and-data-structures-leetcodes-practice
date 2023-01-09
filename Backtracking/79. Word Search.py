from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        self.visit = set()
        self.n_row = len(board)
        self.n_col = len(board[0])
        self.word = word
        self.board = board

        """base case"""
        unique_chars = set(word)
        board_unique_chars = set()
        for row_id in range(len(board)):
            board_unique_chars.update(set(board[0]))

        for char in unique_chars:
            if char not in board_unique_chars:
                return False

        for row_id in range(len(board)):
            for col_id in range(len(board[0])):
                char = board[row_id][col_id]
                if char == word[0]:
                    cell_id = (row_id,  col_id)
                    self.visit.add(cell_id)
                    is_match = self.backtrack([word[0]], row_id, col_id, 1)
                    if is_match:
                        return True
                    else:
                        self.visit.remove(cell_id)

        return False

    def backtrack(self, path, row_id, col_id, word_index):
        # print(path)
        if len(path) == len(self.word):
            # print(path)
            # print(self.word)
            return True

        """if not still satisfy, continue to loop for the word[word_index]"""
        next_points = [(next_row_id, next_col_id) for next_row_id, next_col_id in [(row_id+1, col_id), (row_id-1, col_id),
                                                                                   (row_id, col_id+1), (row_id, col_id-1)] if 0 <= next_row_id < self.n_row and 0 <= next_col_id < self.n_col]
        for next_row_id, next_col_id in next_points:

            cell_id = (next_row_id, next_col_id)
            if cell_id in self.visit:
                """It's been visited"""
                continue

            """criteria to add char into path"""
            char = self.board[next_row_id][next_col_id]
            if word_index < len(self.word) and self.word[word_index] == char:
                path.append(char)
                self.visit.add(cell_id)
                is_match = self.backtrack(
                    path, next_row_id, next_col_id, word_index+1)
                if is_match:
                    return True
                else:
                    """unselect"""
                    _ = path.pop(-1)
                    self.visit.remove(cell_id)
        return False


if __name__ == "__main__":
    board = [["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], [
        "A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"]]
    word = "AAAAAAAAAAAAAAa"
    print(Solution().exist(board, word))
