class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n ^ (n >> 1)
        return not (x & (x + 1))

    def hasAlternatingBits2(self, n: int) -> bool:
        return (n & (n >> 1)) == 0 and (n & (n >> 2)) == (n >> 2)

    def hasAlternatingBits1(self, n: int) -> bool:
        b = n & 1
        while n > 0:
            if n & 1 != b:
                return False
            n >>= 1
            b = 1 - b
        return True


s = Solution()
print(s.hasAlternatingBits(4))
print(s.hasAlternatingBits(5))
print(s.hasAlternatingBits(7))
print(s.hasAlternatingBits(11))
print(s.hasAlternatingBits(10))
print(s.hasAlternatingBits(100))
print(s.hasAlternatingBits(42))
