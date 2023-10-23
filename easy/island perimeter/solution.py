from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        result = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    result += 4
                    if i > 0 and grid[i - 1][j] == 1:
                        result -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        result -= 2
        return result


s = Solution()
print(s.islandPerimeter(grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
print(s.islandPerimeter(grid=[[1]]))
print(s.islandPerimeter(grid=[[1, 0]]))
