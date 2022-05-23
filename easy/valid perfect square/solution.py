class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while i ** 2 <= num:
            if i ** 2 == num:
                return True
            else:
                i += 1
        return False

    def isPerfectSquare4(self, num: int) -> bool:
        left = 0
        right = num
        while left <= right:
            mid = left + (right - left) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                right = mid - 1
            else:
                left = mid + 1
        return False

    def isPerfectSquare3(self, num: int) -> bool:
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0

    def isPerfectSquare2(self, num: int) -> bool:
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
