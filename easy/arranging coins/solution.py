class Solution:
    def arrangeCoins(self, n: int) -> int:
        result = 0
        step = 1
        while n >= 0:
            n -= step
            result += 1
            step += 1
        return result - 1


s = Solution()
print(s.arrangeCoins(5))
print(s.arrangeCoins(8))
