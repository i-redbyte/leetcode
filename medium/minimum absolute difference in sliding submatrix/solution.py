from typing import List


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        result = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                vals = []
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        vals.append(grid[r][c])

                vals.sort()

                best = float('inf')
                for t in range(1, len(vals)):
                    if vals[t] != vals[t - 1]:
                        best = min(best, vals[t] - vals[t - 1])

                result[i][j] = 0 if best == float('inf') else best

        return result


s = Solution()
print(s.minAbsDiff(grid=[[1, 8], [3, -2]], k=2))
print(s.minAbsDiff(grid=[[3, -1]], k=1))
print(s.minAbsDiff(grid=[[1, -2, 3], [2, 3, 5]], k=2))
