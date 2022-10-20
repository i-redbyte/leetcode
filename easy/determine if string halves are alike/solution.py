class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        alphabet = "aeiouAEIOU"
        start = 0
        end = len(s)
        left = 0
        right = 0
        while start != end:
            end -= 1
            if s[start] in alphabet:
                left += 1
            if s[end] in alphabet:
                right += 1
            start += 1
        return left == right


s = Solution()
print(s.halvesAreAlike("book"))
print(s.halvesAreAlike("textbook"))
print(s.halvesAreAlike("booiok"))
