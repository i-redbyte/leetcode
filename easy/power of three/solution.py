import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        return math.log10(n) / math.log10(3) % 1 == 0


s = Solution()
print(s.isPowerOfThree(27))
print(s.isPowerOfThree(0))
print(s.isPowerOfThree(9))
print(s.isPowerOfThree(243))
print(s.isPowerOfThree(-3))
