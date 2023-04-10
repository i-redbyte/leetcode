class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0
        j = 0
        last = 0
        star = -1
        n = len(p)
        m = len(s)
        while i < m:
            if j < n and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < n and p[j] == '*':
                last = i
                star = j
                j += 1
            elif star != -1:
                j = star + 1
                i = last + 1
                last += 1
            else:
                return False
        while j < n and p[j] == '*':
            j += 1
        return j == n

    def isMatch1(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for j in range(1, m + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[n][m]


s = Solution()
print(s.isMatch(s="aa", p="a"))
print(s.isMatch(s="aa", p="*"))
print(s.isMatch(s="cb", p="?a"))
