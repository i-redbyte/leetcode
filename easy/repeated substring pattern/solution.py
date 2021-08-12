class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0 and s[:i] * (n // i) == s:
                return True
        return False


s = Solution()

print(s.repeatedSubstringPattern("abab"))
print(s.repeatedSubstringPattern("aba"))
print(s.repeatedSubstringPattern("abcabcabcabc"))
