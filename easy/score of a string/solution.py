class Solution:
    def scoreOfString(self, s: str) -> int:
        result = 0
        n = len(s)
        for i in range(1, n):
            result += abs(ord(s[i]) - ord(s[i - 1]))
        return result


s = Solution()
print(s.scoreOfString("hello"))
print(s.scoreOfString("zaz"))
print(s.scoreOfString("ww"))
print(s.scoreOfString("dddd"))
