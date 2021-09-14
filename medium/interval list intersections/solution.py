from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        while firstList and secondList:
            i = firstList[0]
            j = secondList[0]
            if i[1] >= j[0] and i[0] <= j[1]:
                result.append([max(i[0], j[0]), min(i[1], j[1])])
            if i[1] < j[1]:
                firstList.pop(0)
            else:
                secondList.pop(0)
        return result


s = Solution()
print(s.intervalIntersection([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]))
print(s.intervalIntersection([[1, 3], [5, 9]], []))
print(s.intervalIntersection([], [[4, 8], [10, 12]]))
print(s.intervalIntersection([[1, 7]], [[3, 10]]))
print(s.intervalIntersection([], []))
