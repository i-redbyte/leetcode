class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        mask = ~0
        while n & mask:
            mask <<= 1
        return ~mask & ~n

    def bitwiseComplement1(self, n: int) -> int:
        return (1 << len(bin(n)) - 2) - 1 - n


print(Solution().bitwiseComplement(5))
print(Solution().bitwiseComplement(7))
print(Solution().bitwiseComplement(10))
print(Solution().bitwiseComplement(0))
