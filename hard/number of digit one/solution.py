class Solution:
    def countDigitOne(self, n: int) -> int:
        if n == 0:
            return 0
        result = 0
        result += int((n - 1) / 10) + 1
        i = 1
        while 10 ** i <= n:
            result += 10 ** i * int(n / 10 ** (i + 1)) + min(10 ** i, max(n % 10 ** (i + 1) - 10 ** i + 1, 0))
            i += 1
        return result


s = Solution()
print(s.countDigitOne(13))
print(s.countDigitOne(0))
print(s.countDigitOne(1))
