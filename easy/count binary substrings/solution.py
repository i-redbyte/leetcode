class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        result = 0
        prev = 0
        current = 1
        n = len(s)
        for i in range(1, n):
            if s[i - 1] != s[i]:
                result += min(prev, current)
                prev = current
                current = 1
            else:
                current += 1
        return result + min(prev, current)


s = Solution()
print(s.countBinarySubstrings("00110011"))
print(s.countBinarySubstrings("10101"))
print(s.countBinarySubstrings("11111"))
