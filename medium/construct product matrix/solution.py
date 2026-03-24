from typing import List

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        result = [[0] * m for _ in range(n)]

        suf = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                result[i][j] = suf
                suf = (suf * grid[i][j]) % MOD

        pre = 1
        for i in range(n):
            for j in range(m):
                result[i][j] = (result[i][j] * pre) % MOD
                pre = (pre * grid[i][j]) % MOD

        return result

s = Solution()
print(s.constructProductMatrix(grid=[[1, 2], [3, 4]]))
print(s.constructProductMatrix(grid=[[12345], [2], [1]]))
