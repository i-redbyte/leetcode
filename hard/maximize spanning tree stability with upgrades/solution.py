from typing import List


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:

        class DSU:
            def __init__(self, n):
                self.p = list(range(n))
                self.r = [0] * n

            def find(self, x):
                if self.p[x] != x:
                    self.p[x] = self.find(self.p[x])
                return self.p[x]

            def union(self, a, b):
                pa, pb = self.find(a), self.find(b)
                if pa == pb:
                    return False
                if self.r[pa] < self.r[pb]:
                    pa, pb = pb, pa
                self.p[pb] = pa
                if self.r[pa] == self.r[pb]:
                    self.r[pa] += 1
                return True

        def can(x):
            dsu = DSU(n)
            used = 0
            upgrades = 0
            upgrade_edges = []

            # обязательные ребра
            for u, v, w, must in edges:
                if must:
                    if w < x:
                        return False
                    if not dsu.union(u, v):  # ← FIX
                        return False
                    used += 1

            # обычные
            for u, v, w, must in edges:
                if must:
                    continue

                if w >= x:
                    if dsu.union(u, v):
                        used += 1
                elif 2 * w >= x:
                    upgrade_edges.append((u, v))

            for u, v in upgrade_edges:
                if used == n - 1 or upgrades == k:
                    break
                if dsu.union(u, v):
                    used += 1
                    upgrades += 1

            return used == n - 1

        lo, hi = 0, 2 * 10 ** 9
        result = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                result = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return result


s = Solution()
print(s.maxStability(n=3, edges=[[0, 1, 2, 1], [1, 2, 3, 0]], k=1))
print(s.maxStability(n=3, edges=[[0, 1, 4, 0], [1, 2, 3, 0], [0, 2, 1, 0]], k=2))
print(s.maxStability(n=3, edges=[[0, 1, 1, 1], [1, 2, 1, 1], [2, 0, 1, 1]], k=0))
