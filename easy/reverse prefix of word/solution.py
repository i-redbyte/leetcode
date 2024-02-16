class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        mask = 0
        i = 0
        while i < len(word) and word[i] != ch:
            mask |= 1 << i
            i += 1

        if i == len(word):
            return word

        mask |= 1 << i
        result = ""
        for j in range(len(word)):
            if mask & (1 << j):
                result += word[i - j]
            else:
                result += word[j]
        return result

    def reversePrefix1(self, word: str, ch: str) -> str:
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
