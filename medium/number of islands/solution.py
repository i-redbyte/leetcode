from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    self.computation(grid, i, j, n, m)
                    result += 1
        return result

    def computation(self, grid: List[List[str]], i: int, j: int, n: int, m: int):
        if (i >= n or j >= m or i < 0 or j < 0) or grid[i][j] != "1":
            return
        grid[i][j] = "-1"
        self.computation(grid, i + 1, j, n, m)
        self.computation(grid, i - 1, j, n, m)
        self.computation(grid, i, j + 1, n, m)
        self.computation(grid, i, j - 1, n, m)


s = Solution()
print(s.numIslands(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))
print(s.numIslands(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))

print(s.numIslands(grid=[
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))

print(s.numIslands([["1", "0", "1", "1", "0", "1", "1"]]))
