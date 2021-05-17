class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        result = 0
        while num >= 10:
            result = 0
            while num > 0:
                x = num % 10
                result += x
                num = num // 10
            num = result
        return result


s = Solution()
print(s.addDigits(100000))
print(s.addDigits(100029))
print(s.addDigits(123))
print(s.addDigits(9))
print(s.addDigits(10))
print(s.addDigits(38))
