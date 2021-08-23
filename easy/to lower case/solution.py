class Solution:
    def toLowerCase(self, s: str) -> str:
        n = len(s)
        space = ord(' ')
        result = list(s)
        for i in range(0, n):
            if "A" <= result[i] <= "Z":
                result[i] = chr(ord(result[i]) + space)
        return "".join(result)


s = Solution()
print(s.toLowerCase("Hello"))
print(s.toLowerCase("here"))
print(s.toLowerCase("LOVELY"))
print(s.toLowerCase(" "))
print(s.toLowerCase("C++"))
print(s.toLowerCase("ASSEMBLER"))
print(s.toLowerCase("ZZZYYYxxxXXX"))
