class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        a = 0
        for i in num1:
            a = a * 10 + ord(i) - ord('0')
        b = 0
        for i in num2:
            b = b * 10 + ord(i) - ord('0')
        c = a + b
        if c == 0:
            return "0"
        result = ""
        while c > 0:
            m = c % 10
            c = c // 10
            result += chr(m + ord('0'))
        return result[::-1]


s = Solution()
print(s.addStrings("123", "11"))
print(s.addStrings("2", "2"))
print(s.addStrings("99999999", "1"))
print(s.addStrings("99999999", "19816237"))
print(s.addStrings("0", "0"))
