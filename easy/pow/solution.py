import math


class Solution:
    def myPow(self, x: float, n: int) -> float:
        p = 1
        if x < 0 and n % 2 != 0:
            p = -1
        return math.exp(n * math.log(abs(x))) * p


s = Solution()
print(s.myPow(2, 10))
print(s.myPow(4, 1))
print(s.myPow(2, -2))
print(s.myPow(-2, 3))
print(s.myPow(4, 2))
print(s.myPow(2.10000, 3))
