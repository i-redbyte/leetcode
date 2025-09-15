from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        total_or = 0
        for x in nums:
            total_or |= x
        if total_or < k:
            return -1

        by = 32
        cnt = [0] * by
        cur_or = 0

        def add(x: int):
            nonlocal cur_or
            b = 0
            while x:
                if x & 1:
                    if cnt[b] == 0:
                        cur_or |= (1 << b)
                    cnt[b] += 1
                x >>= 1
                b += 1

        def remove(x: int):
            nonlocal cur_or
            b = 0
            while x:
                if x & 1:
                    cnt[b] -= 1
                    if cnt[b] == 0:
                        cur_or &= ~(1 << b)
                x >>= 1
                b += 1

        n = len(nums)
        ans = n + 1
        l = 0
        for r in range(n):
            add(nums[r])
            while l <= r and cur_or >= k:
                ans = min(ans, r - l + 1)
                remove(nums[l])
                l += 1

        return ans if ans <= n else -1


s = Solution()
print(s.minimumSubarrayLength(nums=[1, 2, 3], k=2))
print(s.minimumSubarrayLength(nums=[2, 1, 8], k=10))
print(s.minimumSubarrayLength(nums=[1, 2], k=0))
