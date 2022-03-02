class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        n = len(s)
        buffer = [False] * n
        counter = 0
        for c in t:
            if counter < n and c == s[counter]:
                buffer[counter] = True
                counter += 1
        return buffer[n - 1]


s = Solution()
print(s.isSubsequence("abc", "ahbgdc"))
print(s.isSubsequence(s="axc", t="ahbgdc"))
