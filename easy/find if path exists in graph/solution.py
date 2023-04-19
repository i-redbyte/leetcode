import collections
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = [False] * n
        seen[source] = True
        queue = collections.deque([source])

        while queue:
            curr_node = queue.popleft()
            if curr_node == destination:
                return True
            for next_node in graph[curr_node]:
                if not seen[next_node]:
                    seen[next_node] = True
                    queue.append(next_node)

        return False


s = Solution()
print(s.validPath(n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2))
print(s.validPath(n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5))
