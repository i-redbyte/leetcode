class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 4 and p[0] == p[2] and p[1] == '*' and p[3] == '*':
            pattern = p[2:]

        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or
                    first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])


s = Solution()
print(s.isMatch("a", "a"))
print(s.isMatch("aa", "a"))
print(s.isMatch("aa", "a*"))
print(s.isMatch("aa", ".*"))
print(s.isMatch("aab", "c*a*b"))
print(s.isMatch("mississippi", "mis*is*p*."))
