from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        line = [0] * n
        for r in grid:
            if r[0]:
                for i in range(n):
                    line[i] += r[i]
            else:
                for i in range(n):
                    line[i] += 1 - r[i]
        result = 0
        for i in range(n):
            result += max(line[-1 - i], m - line[-1 - i]) * (1 << i)
        return result


s = Solution()
print(s.matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]))
print(s.matrixScore([[0]]))
