class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n > 0:
            n = n // 5
            res += n
        return res


s = Solution()

print(s.trailingZeroes(100))
print(s.trailingZeroes(3))
print(s.trailingZeroes(5))
print(s.trailingZeroes(0))
print(s.trailingZeroes(10))
print(s.trailingZeroes(10000))
