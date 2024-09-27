from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook_position = 0
        pawns = 0
        bishops = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                bit_position: int = (i * 8 + j)
                if board[i][j] == 'R':
                    rook_position |= (1 << bit_position)
                elif board[i][j] == 'p':
                    pawns |= (1 << bit_position)
                elif board[i][j] == 'B':
                    bishops |= (1 << bit_position)

        result = 0

        def check_direction(shift: int, mask_limit: int) -> None:
            nonlocal result
            mask: int = rook_position
            while True:
                mask = (mask << shift) if shift > 0 else (mask >> -shift)

                if mask & mask_limit == 0:
                    break
                if mask & (pawns | bishops):
                    if mask & pawns:
                        result += 1
                    break
                if mask == 0:
                    break

        row_mask = 0xFF
        current_row_mask = row_mask << ((rook_position.bit_length() // 8) * 8)

        check_direction(1, current_row_mask)
        check_direction(-1, current_row_mask)
        check_direction(8, 0xFFFFFFFFFFFFFFFF)
        check_direction(-8, 0xFFFFFFFFFFFFFFFF)

        return result

    def numRookCaptures1(self, board: List[List[str]]) -> int:
        rook_row = 0
        rook_col = 0
        result = 0
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == "R":
                    rook_row = i
                    rook_col = j
                    break
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for dir in directions:
            r = rook_row
            c = rook_col
            while r in range(8) and c in range(8):
                r += dir[0]
                c += dir[1]
                if r not in range(8) or c not in range(8) or board[r][c] == 'B':
                    break
                if board[r][c] == 'p':
                    result += 1
                    break
        return result


s = Solution()
print(s.numRookCaptures([[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
                         [".", ".", ".", "R", ".", ".", ".", "p"], [".", ".", ".", ".", ".", ".", ".", "."],
                         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
                         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]))
print(s.numRookCaptures([[".", ".", ".", ".", ".", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."],
                         [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "B", "R", "B", "p", ".", "."],
                         [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."],
                         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]))
print(s.numRookCaptures([[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
                         [".", ".", ".", "p", ".", ".", ".", "."], ["p", "p", ".", "R", ".", "p", "B", "."],
                         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."],
                         [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]))
