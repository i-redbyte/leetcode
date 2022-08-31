from functools import lru_cache
from typing import List


class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [99999999999] * (1 << n)
        dp[0] = 0
        mask = 0
        while mask < (1 << n):
            bitset = bin(mask).count("1")
            for i in range(n):
                if not ((1 << i) & mask):
                    dp[mask ^ (1 << i)] = min(dp[mask ^ (1 << i)], dp[mask] + (nums1[bitset] ^ nums2[i]))
            mask += 1
        return dp[(1 << n) - 1]

    def minimumXORSum1(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        @lru_cache(None)  # without - Time Limit Exceeded
        def compute(k, val1, val2):
            result = 99999999999
            if k >= n:
                if val1 == val2 == 0:
                    return 0
                else:
                    return 99999999999
            for i in range(n):
                powerTwoI = 2 ** i
                powerTwoK = 2 ** k
                if val2 & powerTwoI and val1 & powerTwoK:
                    result = min(result, (nums1[k] ^ nums2[i]) + compute(k + 1, val1 ^ powerTwoK, val2 ^ powerTwoI))
            return result

        return compute(0, 2 ** n - 1, 2 ** n - 1)


s = Solution()
print(s.minimumXORSum(nums1=[1, 2], nums2=[2, 3]))
print(s.minimumXORSum([1, 0, 3], nums2=[5, 3, 4]))
