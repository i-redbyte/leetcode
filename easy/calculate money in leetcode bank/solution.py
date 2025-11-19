class Solution:
    def totalMoney(self, n: int) -> int:
        week = [1, 2, 3, 4, 5, 6, 7]
        result = 0
        for i in range(n):
            result += week[i % 7]
            week[i % 7] += 1
        return result

    def totalMoney1(self, n: int) -> int:
        w, d = divmod(n, 7)
        return (w * (7 * w + 49) + d * (2 * w + d + 1)) // 2


s = Solution()
print(s.totalMoney(4))
print(s.totalMoney(7))
print(s.totalMoney(10))
print(s.totalMoney(20))  # 96
