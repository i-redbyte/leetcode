from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        result = 0

        def dfs(x: int, y: int, matrix: List[List[int]]) -> None:
            n, m = len(matrix), len(matrix[0])
            if x < 0 or x >= n or y < 0 or y >= m or matrix[x][y] != 0:
                return
            matrix[x][y] = 1
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]
            for k in range(4):
                point_x = x + dx[k]
                point_y = y + dy[k]
                dfs(point_x, point_y, matrix)

        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if (i * j == 0 or i == n - 1 or j == m - 1) and (grid[i][j] == 0):
                    dfs(i, j, grid)

        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if grid[i][j] == 0:
                    dfs(i, j, grid)
                    result += 1
        return result


s = Solution()
print(s.closedIsland(
    grid=[[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 0]]))
print(s.closedIsland(grid=[[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]))
print(s.closedIsland(grid=[[1, 1, 1, 1, 1, 1, 1],
                           [1, 0, 0, 0, 0, 0, 1],
                           [1, 0, 1, 1, 1, 0, 1],
                           [1, 0, 1, 0, 1, 0, 1],
                           [1, 0, 1, 1, 1, 0, 1],
                           [1, 0, 0, 0, 0, 0, 1],
                           [1, 1, 1, 1, 1, 1, 1]]))
