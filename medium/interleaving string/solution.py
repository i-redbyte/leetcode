class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        m, n = len(s1), len(s2)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                else:
                    dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                                dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[-1][-1]


s = Solution()

print(s.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
print(s.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
print(s.isInterleave(s1="", s2="", s3=""))
print(s.isInterleave(s1="a", s2="", s3="c"))
print(s.isInterleave(s1="a", s2="", s3="a"))
print(s.isInterleave(s1="aa", s2="ab", s3="abaa"))
