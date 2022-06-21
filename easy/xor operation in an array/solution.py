class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        for i in range(n):
            result ^= start + 2 * i
        return result


s = Solution()
print(s.xorOperation(5, 0))
print(s.xorOperation(4, 3))
