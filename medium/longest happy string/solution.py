from heapq import heappush, heappop
from collections import deque
from typing import Dict, List, Tuple


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        graph: Dict[str, int] = {'a': a, 'b': b, 'c': c}
        queue = deque(sorted([(count, char) for char, count in graph.items() if count > 0], key=lambda x: -x[0]))
        result = []

        while queue:
            count1, char1 = queue.popleft()
            if len(result) >= 2 and result[-1] == result[-2] == char1:
                if not queue:
                    break
                count2, char2 = queue.popleft()
                result.append(char2)
                count2 -= 1
                if count2 > 0:
                    queue.append((count2, char2))
                queue.append((count1, char1))
            else:
                result.append(char1)
                count1 -= 1
                if count1 > 0:
                    queue.append((count1, char1))

            queue = deque(sorted(queue, key=lambda x: -x[0]))

        return "".join(result)

    def longestDiverseString1(self, a: int, b: int, c: int) -> str:
        max_heap: list[Tuple[int, str]] = []
        if a > 0:
            heappush(max_heap, (-a, 'a'))
        if b > 0:
            heappush(max_heap, (-b, 'b'))
        if c > 0:
            heappush(max_heap, (-c, 'c'))

        result: list[str] = []

        while max_heap:
            count1, char1 = heappop(max_heap)
            if len(result) >= 2 and result[-1] == result[-2] == char1:
                if not max_heap:
                    break
                count2, char2 = heappop(max_heap)
                result.append(char2)
                count2 += 1
                if count2 < 0:
                    heappush(max_heap, (count2, char2))
                heappush(max_heap, (count1, char1))
            else:
                result.append(char1)
                count1 += 1
                if count1 < 0:
                    heappush(max_heap, (count1, char1))

        return "".join(result)


s = Solution()
print(s.longestDiverseString(a=1, b=1, c=7))
print(s.longestDiverseString(a=7, b=1, c=0))
