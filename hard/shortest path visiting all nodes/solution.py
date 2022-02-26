from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        m = len(graph)
        if m == 1:
            return 0
        queue = [(0, 1)]
        for i in range(1, m):
            queue.append((i, 1 << i))
        seen = set(queue)
        # print(seen)
        result = 0
        n = len(queue)
        ending_mask = (1 << m) - 1
        while queue:
            next_queue = []
            for i in range(n):
                node, mask = queue[i]
                for neighbor in graph[node]:
                    next_mask = mask | (1 << neighbor)
                    if next_mask == ending_mask:
                        return result + 1
                    if (neighbor, next_mask) not in seen:
                        seen.add((neighbor, next_mask))
                        next_queue.append((neighbor, next_mask))
            n = len(next_queue)
            result += 1
            queue = next_queue
        return result


s = Solution()
print(s.shortestPathLength([[1, 2, 3], [0], [0], [0]]))
print(s.shortestPathLength([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]))
