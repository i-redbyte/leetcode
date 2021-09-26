from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        current = prices[0]
        n = len(prices)
        for i in range(1, n):
            if current < prices[i]:
                result = max(result, prices[i] - current)
            else:
                current = prices[i]
        return result


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([7, 6, 4, 3, 1]))
print(s.maxProfit([2, 4, 1]))
