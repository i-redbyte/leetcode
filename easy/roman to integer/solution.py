class Solution:
    numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def romanToInt(self, s: str) -> int:
        length = len(s)
        result = int(0)
        i = 0
        while i < length:
            if i + 1 < length:
                left = int(self.numbers.get(s[i], 0))
                right = int(self.numbers.get(s[i + 1], 0))
                if left >= right:
                    result += self.get_value(s[i])
                    step = 1
                else:
                    result += self.get_value(s[i:i + 2])
                    step = 2
            else:
                result += self.get_value(s[i])
                step = 1
            i += step
        return result

    def get_value(self, s: str) -> int:
        if len(s) == 1:
            return self.numbers.get(s, 0)
        left = int(self.numbers.get(s[0], 0))
        right = int(self.numbers.get(s[1], 0))

        if left >= right:
            return left + right
        else:
            return right - left


s = Solution()
print(s.romanToInt("III"))
print(s.romanToInt("IVX"))
print(s.romanToInt("XX"))
print(s.romanToInt("XXI"))
print(s.romanToInt("LVIII"))
print(s.romanToInt("MCMXCIV"))
