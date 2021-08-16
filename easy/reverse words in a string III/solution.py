class Solution:
    def reverseWords2(self, s: str) -> str:
        return " ".join([i[::-1] for i in s.split()])

    def reverseWords(self, s: str) -> str:
        result = ""
        for word in s.split(" "):
            result += self.reverse(word) + " "
        return result[0:-1]

    def reverse(self, s: str) -> str:
        result = ""
        for c in s[::-1]:
            result += c
        return result


s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))
print(s.reverseWords2("Let's take LeetCode contest"))
print(s.reverseWords2("God Ding"))
