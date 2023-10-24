from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        tmp = []
        for val in timeSeries:
            tmp.append((val, 1))
            tmp.append((val + duration, -1))
        result, cur, start = 0, 0, -1
        for val, sign in sorted(tmp):
            if start == -1:
                start = val
            cur += sign
            if not cur:
                result, start = result + val - start, -1
        return result

    def findPoisonedDuration1(self, timeSeries: List[int], duration: int) -> int:
        result = 0
        n = len(timeSeries) - 1
        for i in range(n):
            result += min(timeSeries[i + 1] - timeSeries[i], duration)
        return result + duration


s = Solution()
print(s.findPoisonedDuration(timeSeries=[1, 4], duration=2))
print(s.findPoisonedDuration(timeSeries=[1, 2], duration=2))
