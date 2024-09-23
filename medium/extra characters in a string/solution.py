from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        word_set = set(dictionary)
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            dp[i] = 1 + dp[i + 1]
            for j in range(i + 1, n + 1):
                if s[i:j] in word_set:
                    dp[i] = min(dp[i], dp[j])
        return dp[0]


s = Solution()
print(s.minExtraChar(s="leetscode", dictionary=["leet", "code", "leetcode"]))
print(s.minExtraChar(s="sayhelloworld", dictionary=["hello", "world"]))
print(s.minExtraChar(s="dwmodizxvvbosxxw", dictionary=["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]))
`