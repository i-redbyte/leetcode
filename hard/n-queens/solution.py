from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def getRowCol(i):
            row = i // n
            col = i % n
            return row, col

        def getPos(row, col):
            return row * n + col

        def isValid(row, col, mask):
            for i in range(n):
                if mask & (1 << getPos(row, i)) != 0:
                    return False
                if mask & (1 << getPos(i, col)) != 0:
                    return False

            nr, nc = row + 1, col + 1
            while nr < n and nc < n:
                if mask & (1 << getPos(nr, nc)) != 0:
                    return False
                nr += 1
                nc += 1

            nr, nc = row - 1, col - 1
            while nr >= 0 and nc >= 0:
                if mask & (1 << getPos(nr, nc)) != 0:
                    return False
                nr -= 1
                nc -= 1

            nr, nc = row + 1, col - 1
            while nr < n and nc >= 0:
                if mask & (1 << getPos(nr, nc)) != 0:
                    return False
                nr += 1
                nc -= 1

            nr, nc = row - 1, col + 1
            while nr >= 0 and nc < n:
                if mask & (1 << getPos(nr, nc)) != 0:
                    return False
                nr -= 1
                nc += 1
            return True

        result = []

        def compute(queens, r):
            if r == n:
                result.append(queens)
                return
            for i in range(n):
                if isValid(r, i, queens):
                    compute(queens | (1 << getPos(r, i)), r + 1)

        def toBoard(mask) -> List[List[str]]:
            res = [["."] * n for i in range(n)]
            for i in range(n * n):
                if (1 << i) & mask != 0:
                    r, c = getRowCol(i)
                    res[r][c] = "Q"
            for i in range(len(res)):
                res[i] = "".join(res[i])
            return res

        compute(0, 0)
        result = [toBoard(x) for x in result]
        return result


s = Solution()

print(s.solveNQueens(4))
print(s.solveNQueens(1))
