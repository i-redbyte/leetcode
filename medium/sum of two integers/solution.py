class Solution:
    def getSum(self, a: int, b: int) -> int:
        sign = 0
        if a < 0 and b < 0:
            sign = 1
        mask = 0xffffffff
        result = a ^ b
        carry = (a & b) << 1
        while carry != 0:
            tmp = result
            result = (result ^ carry) & mask
            carry = ((tmp & carry) << 1) & mask
        if sign:
            return ~(result ^ mask)
        return result


s = Solution()
print(s.getSum(-1, 1))
print(s.getSum(1, 2))
print(s.getSum(2, 3))
print(s.getSum(1000, 311))
