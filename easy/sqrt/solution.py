import math


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        return int(math.exp(0.5 * math.log(x)) + 0.00000001)


s = Solution()
print(s.mySqrt(0))
print(s.mySqrt(8))
print(s.mySqrt(4))
print(s.mySqrt(25))
