class Solution:
    def repeatedCharacter(self, s: str) -> str:
        mask = 0
        n = len(s)
        for i in range(n):
            if mask & (1 << (ord(s[i]) - ord('a'))):
                return s[i]
            mask |= (1 << (ord(s[i]) - ord('a')))
        return ""

    def repeatedCharacter2(self, s: str) -> str:
        alphabet = [0] * 26
        for c in s:
            alphabet[ord(c) - ord('a')] += 1
            if alphabet[ord(c) - ord('a')] == 2:
                return c
        return ""

    def repeatedCharacter1(self, s: str) -> str:
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
