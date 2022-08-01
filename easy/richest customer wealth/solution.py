from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        n = len(accounts)
        m = len(accounts[0])
        result = 0
        for i in range(n):
            sum = 0
            for j in range(m):
                sum += accounts[i][j]
            result = max(result, sum)
        return result


s = Solution()

print(s.maximumWealth([[1, 2, 3], [3, 2, 1]]))
print(s.maximumWealth([[1, 5], [7, 3], [3, 5]]))
print(s.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))
