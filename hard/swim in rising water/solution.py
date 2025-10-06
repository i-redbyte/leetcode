from typing import List
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = n * n

        pos = [None] * m
        for r in range(n):
            for c in range(n):
                pos[grid[r][c]] = (r, c)

        parent = list(range(m))
        rank = [0] * m
        active = [False] * m

        def idx(r: int, c: int) -> int:
            return r * n + c

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1

        s = idx(0, 0)
        t = idx(n - 1, n - 1)
        start_t = max(grid[0][0], grid[n - 1][n - 1])

        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for time in range(m):
            r, c = pos[time]
            i = idx(r, c)
            active[i] = True

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    j = idx(nr, nc)
                    if active[j]:
                        union(i, j)

            if time >= start_t and active[s] and active[t] and find(s) == find(t):
                return time

        return -1

    def swimInWater1(self, grid: List[List[int]]) -> int:
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
