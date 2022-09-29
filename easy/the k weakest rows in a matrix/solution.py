from heapq import heappush, heappop
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n = len(mat[0])
        h = []
        for r, row in enumerate(mat):
            if row[-1] == 0:
                heappush(h, (row.index(0), r))
            else:
                heappush(h, (n, r))
        result = [0] * k
        for i in range(k):
            _, result[i] = heappop(h)
        return result


s = Solution()
print(
    s.kWeakestRows(
        mat=
        [[1, 1, 0, 0, 0],
         [1, 1, 1, 1, 0],
         [1, 0, 0, 0, 0],
         [1, 1, 0, 0, 0],
         [1, 1, 1, 1, 1]],
        k=3
    )
)
