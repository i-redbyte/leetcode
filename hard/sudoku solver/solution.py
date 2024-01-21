from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_valid(row, col, num):
            # Check if the number is not in the given row and column
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False

            # Check if the number is not in the given 3x3 box
            startRow, startCol = 3 * (row // 3), 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if board[startRow + i][startCol + j] == num:
                        return False
            return True

        def solve():
            # Find the first empty cell
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        # Try placing numbers 1-9 in the empty cell
                        for num in '123456789':
                            if is_valid(row, col, num):
                                board[row][col] = num
                                if solve():  # Continue with this placement
                                    return True
                                board[row][col] = '.'  # Backtrack
                        return False  # No valid number found, need to backtrack
            return True  # All cells filled

        solve()
        return


s = Solution()

print(s.solveSudoku(
    board=[["5", "3", ".", ".", "7", ".", ".", ".", "."],
           ["6", ".", ".", "1", "9", "5", ".", ".", "."],
           [".", "9", "8", ".", ".", ".", ".", "6", "."],
           ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
           ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
           ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
           [".", "6", ".", ".", ".", ".", "2", "8", "."],
           [".", ".", ".", "4", "1", "9", ".", ".", "5"],
           [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

))
