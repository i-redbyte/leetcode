from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        result = 0.0

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                for k in range(j + 1, n):
                    x3, y3 = points[k]
                    area = abs(
                        x1 * (y2 - y3) +
                        x2 * (y3 - y1) +
                        x3 * (y1 - y2)
                    ) / 2.0
                    if area > result:
                        result = area

        return result


s = Solution()
print(s.largestTriangleArea(points=[[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]))
print(s.largestTriangleArea(points=[[1, 0], [0, 0], [0, 1]]))
