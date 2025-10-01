class Solution:
    def countOdds(self, low: int, high: int) -> int:
        result = 0
        if (low & 1 == 1) or (high & 1 == 1):
            result = 1
        return result + (high - low) // 2


s = Solution()
print(s.countOdds(low=3, high=7))
print(s.countOdds(low=8, high=10))
print(s.countOdds(low=2, high=8))
print(s.countOdds(low=1, high=8))
print(s.countOdds(low=1, high=9))
