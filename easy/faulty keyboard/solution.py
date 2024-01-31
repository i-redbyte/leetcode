class Solution:
    def finalString(self, s: str) -> str:
        result = ""
        for char in s:
            if char == 'i':
                result = result[::-1]
            else:
                result += char
        return result


s = Solution()
print(s.finalString("string"))
print(s.finalString("poiinter"))
print(s.finalString("asm"))
