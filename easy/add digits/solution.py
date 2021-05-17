class Solution:
    def addDigits(self, num: int) -> int:
        result = 0
        while num >= 10:
            result = 0
            while num > 0:
                x = num % 10
                result += x
                num = num // 10
            num = result
        return result

    def addDigits2(self, num: int) -> int:
        if num < 10:
            return num
        result = num % 9
        if result == 0:
            result = 9
        return result


s = Solution()
print(s.addDigits2(100000))
print(s.addDigits2(100029))
print(s.addDigits2(123))
print(s.addDigits2(9))
print(s.addDigits2(10))
print(s.addDigits2(38))
