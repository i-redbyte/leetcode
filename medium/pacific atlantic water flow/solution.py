from typing import List
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])

        def bfs(starts):
            q = deque(starts)
            seen = set(starts)
            while q:
                r, c = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen:
                        if heights[nr][nc] >= heights[r][c]:
                            seen.add((nr, nc))
                            q.append((nr, nc))
            return seen

        pacific_starts = {(0, c) for c in range(n)} | {(r, 0) for r in range(m)}
        atlantic_starts = {(m - 1, c) for c in range(n)} | {(r, n - 1) for r in range(m)}

        pac = bfs(pacific_starts)
        atl = bfs(atlantic_starts)

        return [[r, c] for r in range(m) for c in range(n) if (r, c) in pac and (r, c) in atl]


s = Solution()
print(s.pacificAtlantic(heights=[[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
print(s.pacificAtlantic(heights=[[1]]))
