class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False
        n = len(a)
        different_symbols = list()
        for i in range(0, n):
            if a[i] != b[i]:
                different_symbols.append((a[i], b[i]))

        if len(different_symbols) == 2:
            return different_symbols[0] == different_symbols[1][::-1]

        if len(different_symbols) == 0:
            return n - len(set(a)) != 0
        return False


s = Solution()
print(s.buddyStrings("ab", "ba"))
print(s.buddyStrings("ab", "ab"))
print(s.buddyStrings("aa", "aa"))
