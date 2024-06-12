class Solution:
    count = 0

    def totalNQueens(self, n: int) -> int:
        self.count = 0
        self.solve(0, n, 0, 0, 0)
        return self.count

    def solve(self, row: int, n: int, cols: int, d1: int, d2: int):
        if row == n:
            self.count += 1
            return
        available_positions = ((1 << n) - 1) & ~(cols | d1 | d2)
        pos = available_positions
        while pos != 0:
            bit = pos & -pos
            pos -= bit
            self.solve(row + 1, n, cols | bit, (d1 | bit) << 1, (d2 | bit) >> 1)


s = Solution()
print(s.totalNQueens(4))
print(s.totalNQueens(1))
print(s.totalNQueens(9))
print(s.totalNQueens(8))
