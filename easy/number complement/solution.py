class Solution:
    def findComplement(self, num: int) -> int:
        return (1 << len(bin(num)) - 2) - 1 - num

    def findComplement2(self, num: int) -> int:
        return num ^ (2 ** num.bit_length() - 1)

    def findComplement1(self, num: int) -> int:
        mask = ~0
        while num & mask:
            mask <<= 1
        return ~mask & ~num


print(Solution().findComplement(5))
print(Solution().findComplement(1))
