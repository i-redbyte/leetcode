class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = 5
        return int(self.fak(n + vowels - 1) / (self.fak(vowels - 1) * self.fak(n)))

    def fak(self, n: int) -> int:
        if n == 0:
            return 1
        return n * self.fak(n - 1)


s = Solution()
print(s.countVowelStrings(1))
print(s.countVowelStrings(2))
print(s.countVowelStrings(33))
