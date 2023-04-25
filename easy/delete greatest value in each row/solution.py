from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        def solution(grid: List[List[int]], result: int) -> int:
            if not grid[0]:
                return result
            current_max = 0
            for line in grid:
                max_value = max(line)
                if max_value >= current_max:
                    current_max = max_value
                line.remove(max_value)

            result += current_max
            return solution(grid, result)

        return solution(grid, 0)

    def deleteGreatestValue1(self, grid: List[List[int]]) -> int:
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
