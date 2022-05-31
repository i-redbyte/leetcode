from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        minx = m
        miny = n
        for a in ops:
            minx = min(minx, a[0])
            miny = min(miny, a[1])
        return minx * miny


s = Solution()
print(s.maxCount(m=3, n=3, ops=[[2, 2], [3, 3]]))
print(s.maxCount(m=3, n=3,
                 ops=[[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3]]))
print(s.maxCount(m=3, n=3, ops=[]))
