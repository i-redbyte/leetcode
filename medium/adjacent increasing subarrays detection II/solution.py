from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        inc_start = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                inc_start[i] = inc_start[i + 1] + 1

        def ok(k: int) -> bool:
            if k == 0:
                return True
            if 2 * k > n:
                return False
            limit = n - 2 * k
            for a in range(limit + 1):
                if inc_start[a] >= k and inc_start[a + k] >= k:
                    return True
            return False

        lo, hi = 0, n // 2
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo


s = Solution()
print(s.maxIncreasingSubarrays([2, 5, 7, 8, 9, 2, 3, 4, 3, 1]))
print(s.maxIncreasingSubarrays([1, 2, 3, 4, 4, 4, 4, 5, 6, 7]))
