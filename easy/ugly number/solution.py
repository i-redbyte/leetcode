class Solution:
    def maxDiv(self, a: int, b: int) -> int:
        while a % b == 0:
            a = a / b
        return a

    def isUgly2(self, n: int) -> bool:
        n = self.maxDiv(n, 2)
        n = self.maxDiv(n, 3)
        n = self.maxDiv(n, 5)
        return n == 1

    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        while n % 3 == 0:
            n /= 3
        while n % 5 == 0:
            n /= 5
        return n == 1


s = Solution()
print(s.isUgly(6))
print(s.isUgly(7))
print(s.isUgly(8))
print(s.isUgly(1))
print(s.isUgly(14))
print(s.isUgly(21))
print(s.isUgly(0))
print(s.isUgly(1))
