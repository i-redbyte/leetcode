from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        if not arrays:
            return 0
        globalMin = arrays[0][0]
        globalMax = arrays[0][-1]
        maxDistance = 0
        n = len(arrays)
        for i in range(1, n):
            currentArray = arrays[i]
            currentMin = currentArray[0]
            currentMax = currentArray[-1]
            maxDistance = max(maxDistance, abs(currentMax - globalMin), abs(globalMax - currentMin))
            globalMin = min(globalMin, currentMin)
            globalMax = max(globalMax, currentMax)

        return maxDistance


s = Solution()
print(s.maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]))
print(s.maxDistance([[1], [1]]))
