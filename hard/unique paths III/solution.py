from typing import List


class Solution:
    def getState(self, i, j, m: int):
        return 1 << (i * m + j)

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        begin = 0
        start = None
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 or grid[i][j] == 2:
                    begin |= self.getState(i, j, m)
                elif grid[i][j] == 1:
                    start = (i, j)

        mem = dict()

        def dfs(x: int, y: int, state: int):
            if grid[x][y] == 2:
                return 0 if state else 1
            if (x, y, state) in mem:
                return mem[(x, y, state)]
            count = 0
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if 0 <= x + dx < n and 0 <= y + dy < m and state & self.getState(x + dx, y + dy, m):
                    count += dfs(x + dx, y + dy, state - self.getState(x + dx, y + dy, m))
            mem[(x, y, state)] = count
            return count

        return dfs(start[0], start[1], begin)


s = Solution()
print(s.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))
print(s.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]))
print(s.uniquePathsIII([[0, 1], [2, 0]]))
print(s.uniquePathsIII([[0, 0, 0, 0, 0, 0, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]))
