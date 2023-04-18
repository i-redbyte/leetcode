from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        result = 0
        n = len(grid)
        m = len(grid[0])
        for j in range(0, n):
            grid[j].sort()
        for i in range(0, m):
            tmp = 0
            for j in range(0, n):
                tmp = max(tmp, grid[j].pop())
            result += tmp
        return result


s = Solution()
print(s.deleteGreatestValue([[1, 2, 4], [3, 3, 1]]))
print(s.deleteGreatestValue([[10]]))
