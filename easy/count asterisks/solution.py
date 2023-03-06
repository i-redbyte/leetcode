class Solution:
    def countAsterisks(self, s: str) -> int:
        inside = False
        result = 0
        for ch in s:
            if not inside and ch == '*':
                result += 1
            if ch == '|':
                inside = not inside
        return result


s = Solution()
print(s.countAsterisks("l|*e*et|c**o|*de|"))
print(s.countAsterisks("iamprogrammer"))
print(s.countAsterisks("yo|uar|e**|b|e***au|tifu|l"))
