from typing import List


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        # d1: prefix sums on diagonal ↘
        # d2: prefix sums on diagonal ↙
        d1 = [[0] * (n + 2) for _ in range(m + 1)]
        d2 = [[0] * (n + 2) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                d1[i][j] = d1[i - 1][j - 1] + grid[i - 1][j - 1]
                d2[i][j] = d2[i - 1][j + 1] + grid[i - 1][j - 1]

        best = set()

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                best.add(grid[i - 1][j - 1])

                max_k = min(i - 1, m - i, j - 1, n - j)
                for k in range(1, max_k + 1):
                    a = d1[i + k][j] - d1[i][j - k]  # left -> bottom
                    b = d1[i][j + k] - d1[i - k][j]  # top -> right
                    c = d2[i][j - k] - d2[i - k][j]  # top -> left
                    d = d2[i + k][j] - d2[i][j + k]  # right -> bottom

                    # correct double-counted / missed vertices
                    total = a + b + c + d - grid[i + k - 1][j - 1] + grid[i - k - 1][j - 1]
                    best.add(total)

        return sorted(best, reverse=True)[:3]


s = Solution()
print(
    s.getBiggestThree(grid=[[3, 4, 5, 1, 3], [3, 3, 4, 2, 3], [20, 30, 200, 40, 10], [1, 5, 5, 4, 1], [4, 3, 2, 2, 5]]))
print(s.getBiggestThree(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(s.getBiggestThree(grid=[[7, 7, 7]]))
