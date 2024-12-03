from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        prev = 0
        for space in spaces:
            result.append(s[prev:space])
            result.append(" ")
            prev = space
        result.append(s[prev:])
        return "".join(result)

    def addSpaces_bad(self, s: str, spaces: List[int]) -> str:
        result = ""
        for i, ch in enumerate(s):
            if i in spaces:
                result += " "
            result += ch
        return result


s = Solution()

print(s.addSpaces(s="LeetcodeHelpsMeLearn", spaces=[8, 13, 15]))
print(s.addSpaces(s="icodeinpython", spaces=[1, 5, 7, 9]))
print(s.addSpaces(s="spacing", spaces=[0, 1, 2, 3, 4, 5, 6]))
