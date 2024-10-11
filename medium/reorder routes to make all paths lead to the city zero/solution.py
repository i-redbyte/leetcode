from collections import defaultdict
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))

        def dfs(node, parent):
            count = 0
            for neighbor, cost in graph[node]:
                if neighbor != parent:
                    count += cost + dfs(neighbor, node)
            return count

        return dfs(0, -1)


s = Solution()
print(s.minReorder(n=6, connections=[[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))
print(s.minReorder(n=5, connections=[[1, 0], [1, 2], [3, 2], [3, 4]]))
print(s.minReorder(n=3, connections=[[1, 0], [2, 0]]))
