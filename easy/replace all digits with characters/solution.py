class Solution:
    def replaceDigits(self, s: str) -> str:
        result = ""
        i = 0
        n = len(s) - 1
        if n == 0:
            return s
        while i < n:
            result += s[i]
            shift = int(s[i + 1]) % 26
            result += chr(ord(s[i]) + shift)
            i += 2
        if i == n and s[i] not in "0123456789":
            result += s[i]
        return result


s = Solution()
print(s.replaceDigits("a1c1e1"))
print(s.replaceDigits("a1b2c3d4e"))
