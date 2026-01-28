from typing import List


class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        INF = 10 ** 18

        dp_prev = [[INF] * n for _ in range(m)]
        dp_prev[0][0] = 0

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                best = INF
                if i:
                    cand = dp_prev[i - 1][j] + grid[i][j]
                    if cand < best:
                        best = cand
                if j:
                    cand = dp_prev[i][j - 1] + grid[i][j]
                    if cand < best:
                        best = cand
                dp_prev[i][j] = best

        for _ in range(k):
            min_cost_by_value = {}
            for i in range(m):
                row_dp = dp_prev[i]
                row_g = grid[i]
                for j in range(n):
                    v = row_g[j]
                    c = row_dp[j]
                    prev = min_cost_by_value.get(v)
                    if prev is None or c < prev:
                        min_cost_by_value[v] = c

            values_desc = sorted(min_cost_by_value.keys(), reverse=True)
            best_ge = {}
            cur_min = INF
            for v in values_desc:
                c = min_cost_by_value[v]
                if c < cur_min:
                    cur_min = c
                best_ge[v] = cur_min

            dp = [[INF] * n for _ in range(m)]
            for i in range(m):
                row_dp_prev = dp_prev[i]
                row_g = grid[i]
                row_dp = dp[i]
                for j in range(n):
                    v = row_g[j]
                    base = row_dp_prev[j]
                    tele = best_ge[v]
                    row_dp[j] = tele if tele < base else base

            for i in range(m):
                for j in range(n):
                    if i == 0 and j == 0:
                        continue
                    best = dp[i][j]
                    if i:
                        cand = dp[i - 1][j] + grid[i][j]
                        if cand < best:
                            best = cand
                    if j:
                        cand = dp[i][j - 1] + grid[i][j]
                        if cand < best:
                            best = cand
                    dp[i][j] = best

            dp_prev = dp

        return dp_prev[m - 1][n - 1]


s = Solution()

print(s.minCost(grid=[[1, 3, 3], [2, 5, 4], [4, 3, 5]], k=2))
print(s.minCost(grid=[[1, 2], [2, 3], [3, 4]], k=1))
