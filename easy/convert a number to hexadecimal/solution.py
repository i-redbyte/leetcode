class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        power = "0123456789abcdef"
        result = ""
        while num != 0 and len(result) < 8:
            result = power[num & 15] + result
            num >>= 4
        return result

    def toHex2(self, num: int) -> str:
        if 0 <= num < 10:
            return str(num)
        result = ""
        power = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
        n = num
        if num < 0:
            n = 4294967296 + num  # n = 2 ** 32 + num
        while n > 0:
            m = n % 16
            if m > 9:
                result = power[m] + result
            else:
                result = str(m) + result
            n = n // 16
        return result


s = Solution()
print(s.toHex(26))
print(s.toHex(-1))
print(s.toHex(0))
print(s.toHex(7))
