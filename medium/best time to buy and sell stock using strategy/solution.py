from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        half = k // 2
        prefixProfit = [0] * (n + 1)
        prefixPrice = [0] * (n + 1)

        for i in range(n):
            prefixProfit[i + 1] = prefixProfit[i] + strategy[i] * prices[i]
            prefixPrice[i + 1] = prefixPrice[i] + prices[i]

        base = prefixProfit[n]
        best_gain = 0

        for s in range(0, n - k + 1):
            window_profit = prefixProfit[s + k] - prefixProfit[s]
            second_half_price = prefixPrice[s + k] - prefixPrice[s + half]
            gain = second_half_price - window_profit
            if gain > best_gain:
                best_gain = gain

        return base + best_gain


s = Solution()
print(s.maxProfit(prices=[4, 2, 8], strategy=[-1, 0, 1], k=2))
print(s.maxProfit(prices=[5, 4, 3], strategy=[1, 1, 0], k=2))
