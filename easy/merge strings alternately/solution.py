class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_s = word1
        max_s = word2
        if len(min_s) > len(max_s):
            min_s, max_s = max_s, min_s
        n = len(min_s)
        result = ""
        for i in range(n):
            result += word1[i] + word2[i]
        result += max_s[n:]
        return result


s = Solution()
print(s.mergeAlternately("abc", "pqr"))
print(s.mergeAlternately("ab", "pqrs"))
print(s.mergeAlternately("abcd", "pq"))
