from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def solution(i: int, j: int, grid: List[List[int]]) -> int:
            if i == 0 and j == 0:
                return grid[0][0]
            if i < 0 or j < 0:
                return 999999999999999999999999
            vertical = grid[i][j] + solution(i - 1, j, grid)
            horizontal = grid[i][j] + solution(i, j - 1, grid)
            return min(horizontal, vertical)

        n, m = len(grid), len(grid[0])
        return solution(n - 1, m - 1, grid)

    def minPathSum1(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        for i in range(1, n):
            grid[i][0] += grid[i - 1][0]

        for i in range(1, m):
            grid[0][i] += grid[0][i - 1]

        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]


s = Solution()
print(s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(s.minPathSum([[1, 2, 3], [4, 5, 6]]))
