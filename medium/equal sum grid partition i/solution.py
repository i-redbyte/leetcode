from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        total = 0
        for row in grid:
            total += sum(row)

        if total % 2 != 0:
            return False

        target = total // 2

        # горизонтальный разрез
        pref = 0
        for i in range(m - 1):
            pref += sum(grid[i])
            if pref == target:
                return True

        # вертикальный разрез
        pref = 0
        for j in range(n - 1):
            col_sum = 0
            for i in range(m):
                col_sum += grid[i][j]
            pref += col_sum
            if pref == target:
                return True

        return False


s = Solution()
print(s.canPartitionGrid(grid=[[1, 4], [2, 3]]))
print(s.canPartitionGrid(grid=[[1, 3], [2, 4]]))
