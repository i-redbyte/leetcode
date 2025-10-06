from typing import List
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pq = [(grid[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while pq:
            t, r, c = heapq.heappop(pq)
            if visited[r][c]:
                continue
            visited[r][c] = True
            if r == n - 1 and c == n - 1:
                return t
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    nt = max(t, grid[nr][nc])
                    heapq.heappush(pq, (nt, nr, nc))


s = Solution()
print(s.swimInWater(grid=[[0, 2], [1, 3]]))
print(s.swimInWater(
    grid=[[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]))
