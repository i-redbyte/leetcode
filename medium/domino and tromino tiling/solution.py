class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 1000000007
        if n <= 2:
            return n
        previous = 1
        result = 2
        current = 1
        for k in range(3, n + 1):
            tmp = result
            result = (result + previous + 2 * current) % MOD
            current = (current + previous) % MOD
            previous = tmp
        return result


s = Solution()

print(s.numTilings(3))
print(s.numTilings(1))
