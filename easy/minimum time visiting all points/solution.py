from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        n = len(points)
        for i in range(1, n):
            temp1 = abs(points[i][0] - points[i - 1][0])
            temp2 = abs(points[i][1] - points[i - 1][1])
            result += max(temp1, temp2)
        return result


s = Solution()
print(s.minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]]))
print(s.minTimeToVisitAllPoints([[3, 2], [-2, 2]]))
