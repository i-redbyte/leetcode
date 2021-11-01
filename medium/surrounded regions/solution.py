from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        if rows <= 2:
            return None

        cols = len(board[0])
        if cols <= 2:
            return None

        def replace(i: int, j: int):
            if i < 0 or i > rows - 1 or j < 0 or j > cols - 1:
                return
            if board[i][j] != 'O':
                return

            board[i][j] = '*'
            replace(i, j + 1)
            replace(i, j - 1)
            replace(i + 1, j)
            replace(i - 1, j)

        for i in range(rows):
            replace(i, 0)
            replace(i, cols - 1)

        for i in range(cols):
            replace(0, i)
            replace(rows - 1, i)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '*':
                    board[i][j] = 'O'
