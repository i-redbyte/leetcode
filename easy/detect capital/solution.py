class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        up_set = set("QWERTYUIOPLKJHGFDSAZXCVBNM")
        low_set = set("qwertyuioplkjhgfdsazxcvbnm")
        word_set = set(word)
        sub_set = word_set - up_set
        n = len(sub_set)
        w = len(word_set)
        if not n or n == w:
            return True
        if word[0] in up_set:
            if not set(word[1:]) - low_set:
                return True
        return False

    def detectCapitalUse1(self, word: str) -> bool:
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
