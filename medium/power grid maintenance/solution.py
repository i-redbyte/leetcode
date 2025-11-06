from typing import List
import heapq


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        parent = list(range(c + 1))
        rank = [0] * (c + 1)

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

        for u, v in connections:
            union(u, v)

        heaps = [[] for _ in range(c + 1)]
        for node in range(1, c + 1):
            root = find(node)
            heapq.heappush(heaps[root], node)

        online = [True] * (c + 1)

        result: List[int] = []

        for t, x in queries:
            if t == 2:
                online[x] = False
            else:  # t == 1
                if online[x]:
                    result.append(x)
                else:
                    root = find(x)
                    h = heaps[root]
                    while h and not online[h[0]]:
                        heapq.heappop(h)
                    if not h:
                        result.append(-1)
                    else:
                        result.append(h[0])

        return result


s = Solution()
print(s.processQueries(c=5, connections=[[1, 2], [2, 3], [3, 4], [4, 5]],
                       queries=[[1, 3], [2, 1], [1, 1], [2, 2], [1, 2]]))
print(s.processQueries(c=3, connections=[], queries=[[1, 1], [2, 1], [1, 1]]))
