class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word_len = 0
        trim_text = s.rstrip()
        n = len(trim_text)
        if n == 0:
            return 0
        i = 0
        while i < n:
            i += 1
            if trim_text[n - i] != ' ':
                last_word_len += 1
            else:
                return last_word_len
        return last_word_len


s = Solution()

print(s.lengthOfLastWord("Hello word!"))
print(s.lengthOfLastWord("   "))
print(s.lengthOfLastWord("Hello"))
print(s.lengthOfLastWord("a"))
print(s.lengthOfLastWord("1 2 3 "))
print(s.lengthOfLastWord("800000 USSR"))
