class Solution:
    def divisorGame(self, n: int) -> bool:
        return n & 1 == 0  # or n % 2 == 0


s = Solution()
print(s.divisorGame(2))
print(s.divisorGame(3))
print(s.divisorGame(11))
print(s.divisorGame(50))
