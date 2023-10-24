from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        result = 0
        n = len(timeSeries) - 1
        for i in range(n):
            result += min(timeSeries[i + 1] - timeSeries[i], duration)
        return result + duration


s = Solution()
print(s.findPoisonedDuration(timeSeries=[1, 4], duration=2))
print(s.findPoisonedDuration(timeSeries=[1, 2], duration=2))
