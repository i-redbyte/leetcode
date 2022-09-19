from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        dp = [0] * (m + 1)
        for op in range(m - 1, -1, -1):
            next_row = dp.copy()
            for left in range(op, -1, -1):
                dp[left] = max(multipliers[op] * nums[left] + next_row[left + 1],
                               multipliers[op] * nums[n - 1 - (op - left)] + next_row[left])
        return dp[0]


s = Solution()
print(s.maximumScore(nums=[1, 2, 3], multipliers=[3, 2, 1]))
print(s.maximumScore(nums=[-5, -3, -3, -2, 7, 1], multipliers=[-10, -5, 3, 4, 6]))
