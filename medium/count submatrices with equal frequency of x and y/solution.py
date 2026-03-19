from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        px = [[0] * (n + 1) for _ in range(m + 1)]
        py = [[0] * (n + 1) for _ in range(m + 1)]
        result = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                px[i][j] = px[i - 1][j] + px[i][j - 1] - px[i - 1][j - 1]
                py[i][j] = py[i - 1][j] + py[i][j - 1] - py[i - 1][j - 1]

                if grid[i - 1][j - 1] == 'X':
                    px[i][j] += 1
                elif grid[i - 1][j - 1] == 'Y':
                    py[i][j] += 1

                if px[i][j] == py[i][j] and px[i][j] > 0:
                    result += 1

        return result


s = Solution()
print(s.numberOfSubmatrices(grid=[["X", "Y", "."], ["Y", ".", "."]]))
print(s.numberOfSubmatrices(grid=[["X", "X"], ["X", "Y"]]))
print(s.numberOfSubmatrices(grid=[[".", "."], [".", "."]]))
