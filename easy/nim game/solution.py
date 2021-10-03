class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


s = Solution()
print(s.canWinNim(4))
print(s.canWinNim(1))
print(s.canWinNim(2))
