from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        n = len(points)
        if n == 1:
            return 1
        points.sort(key=lambda x: x[0])
        # print(points)
        result = n
        current_x2 = points[0][1]
        for i in range(1, n):
            if points[i][0] > current_x2:
                current_x2 = points[i][1]
            else:
                result -= 1
                current_x2 = min(current_x2, points[i][1])
        return result


s = Solution()
print(s.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
print(s.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))
print(s.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))
