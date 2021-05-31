class Solution:
    def makeString(self, s: str) -> str:
        result = []
        for c in s:
            if c != '#':
                result.append(c)
            elif len(result) > 0:
                result.pop()
        return str(result)

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.makeString(s) == self.makeString(t)


s = Solution()
print(s.backspaceCompare("ab#c", "ad#c"))
print(s.backspaceCompare("ab##", "c#d#"))
print(s.backspaceCompare("a##c", "#a#c"))
print(s.backspaceCompare("a#c", "b"))
