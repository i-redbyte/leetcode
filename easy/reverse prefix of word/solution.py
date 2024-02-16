class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = -1
        for i, symbol in enumerate(word):
            if symbol == ch:
                index = i + 1
                break
        if index == -1:
            return word
        return word[:index][::-1] + word[index:]


s = Solution()
print(s.reversePrefix(word="abcdefd", ch="d"))
print(s.reversePrefix(word="xyxzxe", ch="z"))
print(s.reversePrefix(word="abcd", ch="z"))
