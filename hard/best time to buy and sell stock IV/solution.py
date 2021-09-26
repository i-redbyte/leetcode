from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        transactions = [float('-inf')] * ((k * 2) + 1)
        transactions[0] = 0
        n = len(transactions)
        for i in prices:
            for j in range(1, n):
                if j % 2 == 1:
                    transactions[j] = max(transactions[j], transactions[j - 1] - i)
                else:
                    transactions[j] = max(transactions[j], transactions[j - 1] + i)
        return int(transactions[-1])


s = Solution()
print(s.maxProfit(2, [2, 4, 1]))
print(s.maxProfit(7, [3, 2, 6, 5, 0, 3]))
