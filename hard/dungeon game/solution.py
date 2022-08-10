from functools import cache
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        @cache # for exclude: Time Limit Exceeded
        def dp(i, j):
            if (i, j) in ((m - 1, n), (m, n - 1)):
                return 1
            if i == m or j == n:
                return 9999999
            return max(min(dp(i + 1, j), dp(i, j + 1)) - dungeon[i][j], 1)

        m, n = len(dungeon), len(dungeon[0])
        return dp(0, 0)


s = Solution()

print(s.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
print(s.calculateMinimumHP([[0]]))
