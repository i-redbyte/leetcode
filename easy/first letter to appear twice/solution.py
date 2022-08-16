class Solution:
    def repeatedCharacter(self, s: str) -> str:
        tmp = set()
        for (i, c) in enumerate(s):
            if c in tmp:
                return c
            tmp.add(c)
        return ""


s = Solution()
print(s.repeatedCharacter("abccbaacz"))
print(s.repeatedCharacter("abcdd"))
print(s.repeatedCharacter("eabcddee"))
