from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        while n % 4 == 0:
            n //= 4
        if n % 8 == 7:
            return 4
        for a in range(int(sqrt(n)) + 1):
            b = int(sqrt(n - a * a))
            if (a ** 2 + b ** 2) == n:
                return (a > 0) + (b > 0)
        return 3

    def numSquares1(self, n: int) -> int:  # Time Limit Exceeded
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        for i in range(0, n + 1):
            j = 1
            while i + j * j <= n:
                dp[i + j * j] = min(dp[i + j * j], dp[i] + 1)
                j += 1
        return int(dp[n])


s = Solution()
print(s.numSquares(12))
print(s.numSquares(13))
