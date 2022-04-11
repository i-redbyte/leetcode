from functools import lru_cache
from typing import List


class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        ans = 0
        X = tuple([2] * numSlots)
        for j in range(1, numSlots + 1):
            if j in nums and X[j - 1] > 0:
                X = X[:j - 1] + (X[j - 1] - 1,) + X[j:]
                nums.remove(j)
                ans += j
        n = len(nums)

        @lru_cache(None)
        def dp(curr, i):
            if i == n:
                return 0
            return max(
                (nums[i] & (j + 1)) + dp(curr[:j] + (curr[j] - 1,) + curr[j + 1:], i + 1) for j in range(numSlots) if
                curr[j] > 0)

        return ans + dp(X, 0)

    # Time Limit Exceeded
    def maximumANDSum1(self, nums: List[int], numSlots: int) -> int:
        def dfs(nums, slots) -> int:
            if not nums:
                return 0
            result = 0
            n = len(slots)
            for i in range(1, n):
                if slots[i] > 0:
                    slots[i] -= 1
                    val = (nums[0] & i) + dfs(nums[1:], slots)
                    if val > result:
                        result = val
                    slots[i] += 1
            return result

        slots = [2] * (numSlots + 1)
        return dfs(nums, slots)


print(Solution().maximumANDSum([1, 2, 3, 4, 5, 6], 3))
print(Solution().maximumANDSum([1, 3, 10, 4, 7, 1], 9))
