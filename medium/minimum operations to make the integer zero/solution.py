class Solution:
    def popcount(self, n: int) -> int:
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c

    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(61):
            x = num1 - k * num2
            if x < 0 or x < k:
                continue
            if self.popcount(x) <= k <= x:
                return k
        return -1


s = Solution()
print(s.makeTheIntegerZero(num1=3, num2=-2))
print(s.makeTheIntegerZero(num1=5, num2=7))
print(s.makeTheIntegerZero(num1=135, num2=26))
