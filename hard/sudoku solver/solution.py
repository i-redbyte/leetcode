from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows, cols, boxes = [0] * 9, [0] * 9, [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    val = int(board[r][c]) - 1
                    rows[r] |= (1 << val)
                    cols[c] |= (1 << val)
                    boxes[(r // 3) * 3 + c // 3] |= (1 << val)

        def solve():
            empty = None
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        empty = (r, c)
                        break
                if empty:
                    break

            if not empty:
                return True

            r, c = empty
            box_index = (r // 3) * 3 + c // 3
            for num in range(9):
                if not (rows[r] & (1 << num)) and not (cols[c] & (1 << num)) and not (boxes[box_index] & (1 << num)):
                    board[r][c] = str(num + 1)
                    rows[r] |= (1 << num)
                    cols[c] |= (1 << num)
                    boxes[box_index] |= (1 << num)
                    if solve():
                        return True
                    board[r][c] = '.'
                    rows[r] &= ~(1 << num)
                    cols[c] &= ~(1 << num)
                    boxes[box_index] &= ~(1 << num)
            return False

        solve()
        return

    def solveSudoku1(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_valid(row, col, num):
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False

            startRow, startCol = 3 * (row // 3), 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if board[startRow + i][startCol + j] == num:
                        return False
            return True

        def solve():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for num in '123456789':
                            if is_valid(row, col, num):
                                board[row][col] = num
                                if solve():
                                    return True
                                board[row][col] = '.'
                        return False
            return True

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
