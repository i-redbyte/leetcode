class Solution:
    def countDigits(self, num: int) -> int:
        result = 0
        if num < 10:
            return 1
        save = num
        while num != 0:
            v = num % 10
            if v != 0 and save % v == 0:
                result += 1
            num = num // 10
        return result


s = Solution()
print(s.countDigits(7))
print(s.countDigits(121))
print(s.countDigits(1248))
