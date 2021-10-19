import bisect
import math
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        ret = -math.inf
        n = len(matrix)
        m = len(matrix[0])
        if n > m:
            return self.maxSumSubmatrix([list(a) for a in zip(*matrix)], k)
        col_prefix = [[0] for _ in range(m)]
        for i in range(n):
            for j in range(m):
                col_prefix[j].append(col_prefix[j][-1] + matrix[i][j])
        arr = [0] * (m + 1)
        for i in range(n):
            for i2 in range(i, n):
                for j in range(1, m + 1):
                    arr[j] = arr[j - 1] + col_prefix[j - 1][i2 + 1] - col_prefix[j - 1][i]
                tmp = []
                for a in arr:
                    idx = bisect.bisect_left(tmp, a - k)
                    if 0 <= idx < len(tmp):
                        ret = max(ret, a - tmp[idx])
                    if ret == k:
                        return k
                    bisect.insort_left(tmp, a)
        return ret


s = Solution()
print(s.maxSumSubmatrix([[1, 0, 1], [0, -2, 3]], 2))
print(s.maxSumSubmatrix([[2, 2, -1]], 3))
