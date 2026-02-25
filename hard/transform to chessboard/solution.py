from typing import List


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        full = (1 << n) - 1

        rowMask = 0
        colMask = 0
        for i in range(n):
            rowMask |= board[0][i] << i
            colMask |= board[i][0] << i

        revRowMask = full ^ rowMask
        revColMask = full ^ colMask
        sameRow = 0
        sameCol = 0

        for i in range(n):
            r = 0
            c = 0
            for j in range(n):
                r |= board[i][j] << j
                c |= board[j][i] << j

            if r != rowMask and r != revRowMask:
                return -1
            if c != colMask and c != revColMask:
                return -1
            if r == rowMask:
                sameRow += 1
            if c == colMask:
                sameCol += 1

        def bitcount(x):
            return bin(x).count('1')

        def min_swaps(mask: int, cnt_same: int) -> int:
            ones = bitcount(mask)
            odd_pos = 0xAAAAAAAA & full
            even_pos = 0x55555555 & full
            if n % 2 == 1:
                if abs(n - 2 * ones) != 1 or abs(n - 2 * cnt_same) != 1:
                    return -1

                if ones == n // 2:
                    return (n // 2) - bitcount(mask & odd_pos)
                else:
                    return ((n + 1) // 2) - bitcount(mask & even_pos)
            else:
                if ones != n // 2 or cnt_same != n // 2:
                    return -1

                swaps_start0 = (n // 2) - bitcount(mask & odd_pos)
                swaps_start1 = (n // 2) - bitcount(mask & even_pos)
                return min(swaps_start0, swaps_start1)

        r = min_swaps(rowMask, sameRow)
        c = min_swaps(colMask, sameCol)
        if r == -1 or c == -1:
            return -1
        return r + c


s = Solution()
print(s.movesToChessboard(board=[[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]]))
print(s.movesToChessboard(board=[[0, 1], [1, 0]]))
