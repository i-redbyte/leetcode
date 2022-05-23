class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        result = num
        while result * result > num:
            result = (result + num / result) // 2
        return result * result == num

    def isPerfectSquare1(self, num: int) -> bool:
        bit = 1 << 15
        result = 0
        while bit > 0:
            result |= bit
            if result > num // result:
                result ^= bit
            bit >>= 1
        return result * result == num


s = Solution()
print(s.isPerfectSquare(16))
print(s.isPerfectSquare(14))
