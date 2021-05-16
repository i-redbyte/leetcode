from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:

        area = 0
        corners = set()
        a = lambda: (Y - y) * (X - x)

        for x, y, X, Y in rectangles:
            area += a()
            corners ^= {(x, y), (x, Y), (X, y), (X, Y)}

        if len(corners) != 4: return False
        x, y = min(corners, key=lambda x: x[0] + x[1])
        X, Y = max(corners, key=lambda x: x[0] + x[1])
        return a() == area


s = Solution()
print(s.isRectangleCover([[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]))
print(s.isRectangleCover([[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]]))
print(s.isRectangleCover([[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [3, 2, 4, 4]]))
print(s.isRectangleCover([[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [2, 2, 4, 4]]))
