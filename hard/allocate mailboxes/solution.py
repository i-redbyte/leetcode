from typing import List


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        n = len(houses)
        houses.sort()
        if k >= n:
            return 0

        prefix = [0] * (n + 1)
        for i, x in enumerate(houses):
            prefix[i + 1] = prefix[i] + x
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                m = (i + j) // 2
                left = houses[m] * (m - i + 1) - (prefix[m + 1] - prefix[i])
                right = (prefix[j + 1] - prefix[m + 1]) - houses[m] * (j - m)
                cost[i][j] = left + right

        INF = 10 ** 18
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for t in range(1, k + 1):
            dp[t][0] = 0
            for j in range(1, n + 1):
                best = INF
                start_p = max(0, t - 1)
                for p in range(start_p, j):
                    cand = dp[t - 1][p] + cost[p][j - 1]
                    if cand < best:
                        best = cand
                dp[t][j] = best

        return dp[k][n]


s = Solution()

print(s.minDistance(houses=[1, 4, 8, 10, 20], k=3))
print(s.minDistance(houses=[2, 3, 5, 12, 18], k=2))
