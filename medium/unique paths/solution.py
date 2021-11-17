import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0
        return int(math.factorial(m + n - 2) / (math.factorial(n - 1) * math.factorial(m - 1)))


s = Solution()
print(s.uniquePaths(3, 7))
print(s.uniquePaths(3, 2))
print(s.uniquePaths(7, 3))
print(s.uniquePaths(3, 3))
