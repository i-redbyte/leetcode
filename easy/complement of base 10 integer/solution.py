class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return (1 << len(bin(n)) - 2) - 1 - n


print(Solution().bitwiseComplement(5))
print(Solution().bitwiseComplement(7))
print(Solution().bitwiseComplement(10))
