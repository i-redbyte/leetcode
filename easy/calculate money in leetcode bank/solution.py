class Solution:
    def totalMoney(self, n: int) -> int:
        w, d = divmod(n, 7)
        return (w * (7 * w + 49) + d * (2 * w + d + 1)) // 2


s = Solution()
print(s.totalMoney(4))
print(s.totalMoney(10))
print(s.totalMoney(20))  # 96
