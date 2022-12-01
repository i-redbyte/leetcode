import heapq
from typing import List


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        result, i = 0, 0
        queue = []
        n = len(apples)
        while i < n or queue:
            if i < n and apples[i] > 0:
                heapq.heappush(queue, [i + days[i], apples[i]])
            while queue and (queue[0][0] <= i or queue[0][1] == 0):
                heapq.heappop(queue)
            if queue:
                queue[0][1] -= 1
                result += 1
            i += 1
        return result


s = Solution()
print(s.eatenApples(apples=[1, 2, 3, 5, 2], days=[3, 2, 1, 4, 2]))
print(s.eatenApples([3, 0, 0, 0, 0, 2], days=[3, 0, 0, 0, 0, 2]))
