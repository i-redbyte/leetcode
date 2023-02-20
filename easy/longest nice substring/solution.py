class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        lower = 0
        upper = 0
        for ch in s:
            if 'a' <= ch <= 'z':
                lower |= 1 << (ord(ch) - ord('a'))
            else:
                upper |= 1 << (ord(ch) - ord('A'))
        for i, ch in enumerate(s):
            if 'a' <= ch <= 'z':
                pos = ord(ch) - ord('a')
            else:
                pos = ord(ch) - ord('A')
            lower_bit = (lower >> pos) & 1
            upper_bit = (upper >> pos) & 1
            if lower_bit ^ upper_bit == 0:
                continue
            s1 = self.longestNiceSubstring(s[0:i])
            s2 = self.longestNiceSubstring(s[i + 1:])
            if len(s1) >= len(s2):
                return s1
            else:
                return s2
        return s


s = Solution()
print(s.longestNiceSubstring("YazaAay"))
print(s.longestNiceSubstring("Bb"))
print(s.longestNiceSubstring("C"))
