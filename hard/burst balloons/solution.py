from functools import lru_cache
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        @lru_cache(None)
        def helper(left, right):
            if left + 1 == right:
                return 0
            res = -99999999999999
            for i in range(left + 1, right):
                res = max(res, nums[i] * nums[left] * nums[right] + helper(left, i) + helper(i, right))
            return res

        return helper(0, len(nums) - 1)


s = Solution()
print(s.maxCoins([3, 1, 5, 8]))
print(s.maxCoins([1, 5]))
