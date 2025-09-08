from typing import List


class Solution:
    def notHasZero(self, x: int) -> bool:
        while x > 9:
            if x % 10 == 0:
                return False
            x = x // 10
        return True

    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(1, n):
            b = n - a
            if self.notHasZero(a) and self.notHasZero(b):
                return [a, b]
        return []


s = Solution()
print(s.getNoZeroIntegers(2))
print(s.getNoZeroIntegers(11))
print(s.getNoZeroIntegers(1010))
