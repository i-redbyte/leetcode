class Solution:
    def repeatedCharacter(self, s: str) -> str:
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
