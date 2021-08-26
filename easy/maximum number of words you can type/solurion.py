class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        result = 0
        words = text.split(" ")
        set_chars = set(brokenLetters)
        for i in words:
            set_word = set(i)
            sub = set_word - set_chars
            if len(set_word) == len(sub):
                result += 1
        return result


s = Solution()
print(s.canBeTypedWords("hello world", "ad"))
print(s.canBeTypedWords("leet code", "lt"))
print(s.canBeTypedWords("leet code", "e"))
print(s.canBeTypedWords("assembly is the best", "z"))
