import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0

        def is_visited(bits: int, idx: int) -> bool:
            return ((bits >> idx) & 1) == 1

        def set_visited(bits: int, idx: int) -> int:
            return bits | (1 << idx)

        maxH = max(max(row) for row in heightMap)
        buckets = [[] for _ in range(maxH + 1)]
        occupancy = 0

        def push(h: int, r: int, c: int):
            nonlocal occupancy
            buckets[h].append((r, c))
            occupancy |= (1 << h)

        def pop_min():
            nonlocal occupancy
            lsb = occupancy & -occupancy
            h = lsb.bit_length() - 1
            r, c = buckets[h].pop()
            if not buckets[h]:
                occupancy &= ~(1 << h)
            return h, r, c

        visited = 0
        trapped = 0

        for r in range(m):
            for c in (0, n - 1):
                idx = r * n + c
                if not is_visited(visited, idx):
                    visited = set_visited(visited, idx)
                    push(heightMap[r][c], r, c)
        for c in range(n):
            for r in (0, m - 1):
                idx = r * n + c
                if not is_visited(visited, idx):
                    visited = set_visited(visited, idx)
                    push(heightMap[r][c], r, c)

        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while occupancy:
            h, r, c = pop_min()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    nidx = nr * n + nc
                    if not is_visited(visited, nidx):
                        visited = set_visited(visited, nidx)
                        nh = heightMap[nr][nc]
                        if nh < h:
                            trapped += h - nh
                        eff = h if h > nh else nh
                        push(eff, nr, nc)

        return trapped

    def trapRainWater1(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0
        result = 0
        visited = [[False] * n for _ in range(m)]
        heap = []

        for r in range(m):
            for c in (0, n - 1):
                heapq.heappush(heap, (heightMap[r][c], r, c))
                visited[r][c] = True
        for c in range(n):
            for r in (0, m - 1):
                if not visited[r][c]:
                    heapq.heappush(heap, (heightMap[r][c], r, c))
                    visited[r][c] = True

        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while heap:
            h, r, c = heapq.heappop(heap)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    nh = heightMap[nr][nc]
                    if nh < h:
                        result += h - nh
                    heapq.heappush(heap, (max(h, nh), nr, nc))

        return result


s = Solution()
print(s.trapRainWater(heightMap=[[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]))
print(s.trapRainWater(heightMap=[[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]))
