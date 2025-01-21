from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        result = float('inf')
        top = sum(grid[0])
        bottom = 0

        n = len(grid[0])
        for i in range(n):
            top -= grid[0][i]
            result = min(result, max(top, bottom))
            bottom += grid[1][i]

        return result


s = Solution()
print(s.gridGame(grid=[[2, 5, 4], [1, 5, 1]]))
print(s.gridGame(grid=[[3, 3, 1], [8, 5, 2]]))
print(s.gridGame(grid=[[1, 3, 1, 15], [1, 3, 3, 1]]))
