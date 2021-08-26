class Solution:
    def countSegments(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            if (i == 0 or s[i - 1] == ' ') and s[i] != ' ':
                result += 1
        return result

    def countSegments2(self, s: str) -> int:
        return len(s.split())


s = Solution()
print(s.countSegments("Hello, my name is John"))
print(s.countSegments("Hello"))
print(s.countSegments("love live! mu'sic forever"))
print(s.countSegments(""))
print(s.countSegments("       f        "))
print(s.countSegments("              "))
print(s.countSegments(", , , ,        a, eaefa"")"))
