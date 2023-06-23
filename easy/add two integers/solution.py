class Solution:
    def sum(self, num1: int, num2: int) -> int:
        mask = 0xFFFFFFFF
        if num2 == 0:
            return num1 if num1 < 0x80000000 else ~(num1 ^ mask)
        carry = ((num1 & num2) << 1) & mask
        non_carry = (num1 ^ num2) & mask
        return self.sum(non_carry, carry)

    def sum1(self, num1: int, num2: int) -> int:
        return num1 + num2


print(Solution().sum(12, 5))
print(Solution().sum(-10, 4))
print(Solution().sum(-100, -100))
