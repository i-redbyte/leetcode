import sys


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        p = 1
        max_int = sys.maxsize * 2 + 1
        while p < max_int:
            if n == p:
                return True
            p = p << 1
        return False

    def isPowerOfTwo1(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0


s = Solution()
print(s.isPowerOfTwo(1))
print(s.isPowerOfTwo(16))
print(s.isPowerOfTwo(3))
print(s.isPowerOfTwo(4))
print(s.isPowerOfTwo(5))
print(s.isPowerOfTwo(128))
