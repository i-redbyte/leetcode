import sys
from typing import List


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        sys.setrecursionlimit(10 ** 7)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        result = 0

        def dfs(u: int, parent: int) -> int:
            nonlocal result
            subtotal = values[u] % k

            for v in g[u]:
                if v == parent:
                    continue
                child_sum = dfs(v, u)
                subtotal = (subtotal + child_sum) % k

            if subtotal == 0:
                result += 1
                return 0
            return subtotal

        dfs(0, -1)
        return result


s = Solution()
print(s.maxKDivisibleComponents(n=5, edges=[[0, 2], [1, 2], [1, 3], [2, 4]], values=[1, 8, 1, 4, 4], k=6))
print(
    s.maxKDivisibleComponents(n=7, edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]], values=[3, 0, 6, 1, 5, 2, 1],
                              k=3))
