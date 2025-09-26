class Solution:
    def smallestNumber1(self, n: int) -> int:
        result = 1
        while n > 0:
            n >>= 1
            result <<= 1
        return result - 1

    def smallestNumber(self, n: int) -> int:
        result = 1
        while result < n:
            result = (result << 1) | 1
        return result


s = Solution()
print(s.smallestNumber(5))
print(s.smallestNumber(4))
print(s.smallestNumber(10))
print(s.smallestNumber(3))
print(s.smallestNumber(2))
print(s.smallestNumber(100))
print(s.smallestNumber(256))
