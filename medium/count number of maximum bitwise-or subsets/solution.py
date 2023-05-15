from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        m = 1 << n
        dp = [-1] * (m)
        dp[0] = 0
        for mask in range(m):
            for j in range(n):
                i = 1 << j
                if mask & i:
                    b = dp[mask ^ i]
                    dp[mask] = b | nums[j]
        return dp.count(max(dp))


s = Solution()
print(s.countMaxOrSubsets([3, 1]))
print(s.countMaxOrSubsets([2, 2, 2]))
print(s.countMaxOrSubsets([3, 2, 1, 5]))
