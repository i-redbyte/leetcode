from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        start = m * n - k % (m * n)
        result = []
        end = m * n + start
        for i in range(start, end):
            j = i % (m * n)
            l = j // n
            t = j % n
            if not (j - start) % n:
                result.append([])
            result[-1].append(grid[l][t])
        return result


s = Solution()
print(s.shiftGrid(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=1))
print(s.shiftGrid(grid=[[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], k=4))
