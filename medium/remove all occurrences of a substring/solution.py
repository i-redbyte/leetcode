class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(part)
        while True:
            index = s.find(part)
            if index == -1:
                break
            s = s[:index] + s[index + n:]
        return s


s = Solution()
print(s.removeOccurrences(s="daabcbaabcbc", part="abc"))
print(s.removeOccurrences(s="axxxxyyyyb", part="xy"))
