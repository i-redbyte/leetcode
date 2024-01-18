class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        counter = 0
        n = len(word)
        for c in word:
            if 'A' <= c <= 'Z':
                counter += 1
        return counter == n or counter == 0 or (counter == 1 and ('A' <= word[0] <= 'Z'))


s = Solution()
print(s.detectCapitalUse("USA"))
print(s.detectCapitalUse("FlaG"))
print(s.detectCapitalUse("leetcode"))
print(s.detectCapitalUse("leetCode"))
print(s.detectCapitalUse("Leetcode"))
print(s.detectCapitalUse("FFFFFFFFFFFFFFFFFFFFf"))
