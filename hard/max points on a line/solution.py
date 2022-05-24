from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        result = 1
        for i in range(n):
            m = {}
            for j in range(n):
                if i == j:
                    continue
                if points[j][0] - points[i][0] == 0:
                    sl = 'pi/2'
                else:
                    sl = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                if sl in m:
                    m[sl] += 1
                else:
                    m[sl] = 2
                result = max(result, m[sl])
        return result


s = Solution()
print(s.maxPoints([[1, 1], [2, 2], [3, 3]]))
print(s.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
