class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


s = Solution()
print(s.reverseWords("the sky is blue"))
print(s.reverseWords("  hello world  "))
print(s.reverseWords("a good   example"))
print(s.reverseWords("  Bob    Loves  Alice   "))
print(s.reverseWords("Alice does not even like bob"))
