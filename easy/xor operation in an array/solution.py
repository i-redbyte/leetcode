class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        last = start + 2 * (n - 1)
        if start % 4 < 2:
            start = 0
        else:
            n -= 1
        if n % 2 == 0:
            return start ^ (n & 2)
        return start ^ last ^ (n & 2)

    def xorOperation1(self, n: int, start: int) -> int:
        result = 0
        for i in range(n):
            result ^= start + 2 * i
        return result


s = Solution()
print(s.xorOperation(5, 0))
print(s.xorOperation(4, 3))
