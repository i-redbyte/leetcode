class Solution:
    def countAsterisks(self, s: str) -> int:
        result = 0
        inside = 0
        for ch in s:
            if ch == '|':
                inside ^= ord(ch)
            if ch == '*' and inside == 0:
                result += 1
        return result

    def countAsterisks2(self, s: str) -> int:
        result = 0
        index = 0
        for world in s.split("|"):
            if index & 1 == 0:
                result += len(world) - len(world.replace("*", ""))
            index += 1
        return result

    def countAsterisks1(self, s: str) -> int:
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
