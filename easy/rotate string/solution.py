class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        if s == goal:
            return True
        for i in range(0, n - 1):
            p = s[1:] + s[0]
            s = p
            if s == goal:
                return True
        return False


s = Solution()
print(s.rotateString('abcde', 'cdeab'))
print(s.rotateString('abcde', 'abced'))
