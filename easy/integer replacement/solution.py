class Solution:
    def integerReplacement(self, n: int) -> int:
        result = 0
        while n != 1:
            if n & 1 == 0:
                n >>= 1
            else:
                if (n - 1) & (1 - n) >= (n + 1) & (-1 - n) or n == 3:
                    n -= 1
                else:
                    n += 1
            result += 1
        return result


s = Solution()
print(s.integerReplacement(8))
print(s.integerReplacement(7))
print(s.integerReplacement(4))
print(s.integerReplacement(65535))
