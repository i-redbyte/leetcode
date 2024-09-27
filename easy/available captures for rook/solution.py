from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
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
