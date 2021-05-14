class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 4:
            return n == 1
        result = 0
        while not (n & 1):
            result += 1
            n = n >> 1
        return not (result & 1) and n == 1


s = Solution()
print(s.isPowerOfFour(16))
print(s.isPowerOfFour(256))
print(s.isPowerOfFour(4))
print(s.isPowerOfFour(5))
print(s.isPowerOfFour(1))
