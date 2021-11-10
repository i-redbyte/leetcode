from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        n = len(prices) - 1
        for i in range(n):
            if prices[i] < prices[i + 1]:
                result += prices[i + 1] - prices[i]
        return result


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([1, 2, 3, 4, 5]))
print(s.maxProfit([7, 6, 4, 3, 1]))
