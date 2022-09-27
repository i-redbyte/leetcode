
class Solution:
    def findComplement(self, num: int) -> int:
        mask = ~0
        while num & mask:
            mask <<= 1
        return ~mask & ~num


print(Solution().findComplement(5))
print(Solution().findComplement(1))
