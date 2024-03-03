from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        k = [releaseTimes[0]]
        n = len(releaseTimes)
        for i in range(1, n):
            k.append(releaseTimes[i] - releaseTimes[i - 1])
        m = max(k)
        l = []
        for i in range(len(k)):
            if k[i] == m:
                l.append(keysPressed[i])
        return max(l)


s = Solution()
print(s.slowestKey([9, 29, 49, 50], keysPressed="cbcd"))
print(s.slowestKey([12, 23, 36, 46, 62], keysPressed="spuda"))
