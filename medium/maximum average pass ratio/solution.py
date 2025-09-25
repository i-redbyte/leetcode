from typing import List
import heapq


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p: int, t: int) -> float:
            return (t - p) / (t * (t + 1))

        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, (-gain(p, t), p, t))

        total = 0.0
        while heap:
            _, p, t = heapq.heappop(heap)
            total += p / t
        return total / len(classes)


s = Solution()

print(s.maxAverageRatio(classes=[[1, 2], [3, 5], [2, 2]], extraStudents=2))
print(s.maxAverageRatio(classes=[[2, 4], [3, 9], [4, 5], [2, 10]], extraStudents=4))
