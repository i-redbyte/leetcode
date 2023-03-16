from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid) - 2
        result = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                result[i][j] = max([grid[k][l] for k in range(i, i + 3) for l in range(j, j + 3)])
        return result


s = Solution()
print(s.largestLocal([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]))
print(s.largestLocal([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]))
