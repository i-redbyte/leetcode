from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        result = 0

        for i in range(m):
            for j in range(n):
                if i > 0:
                    grid[i][j] += grid[i - 1][j]
                if j > 0:
                    grid[i][j] += grid[i][j - 1]
                if i > 0 and j > 0:
                    grid[i][j] -= grid[i - 1][j - 1]

                if grid[i][j] <= k:
                    result += 1

        return result


s = Solution()
print(s.countSubmatrices(grid=[[7, 6, 3], [6, 6, 1]], k=18))
print(s.countSubmatrices(grid=[[7, 2, 9], [1, 5, 0], [2, 6, 6]], k=20))
