class Solution:
    def reverseWords(self, s: str) -> str:
        s = " ".join(s.split())
        words = s.split(" ")
        n = len(words)
        m = n // 2
        for i in range(m):
            words[i], words[n - i - 1] = words[n - i - 1], words[i]
        return " ".join(words)

    def reverseWords1(self, s: str) -> str:
        return " ".join(s.split()[::-1])


s = Solution()
print(s.reverseWords("the sky is blue"))
print(s.reverseWords("  hello world  "))
print(s.reverseWords("a good   example"))
print(s.reverseWords("  Bob    Loves  Alice   "))
print(s.reverseWords("Alice does not even like bob"))
