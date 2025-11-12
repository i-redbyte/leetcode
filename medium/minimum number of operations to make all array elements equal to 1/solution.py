from typing import List
from math import gcd


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        if ones > 0:
            return n - ones

        g_all = nums[0]
        for x in nums[1:]:
            g_all = gcd(g_all, x)
        if g_all != 1:
            return -1

        INF = 9999999999
        best = INF

        for i in range(n):
            g = nums[i]
            for j in range(i + 1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    best = min(best, j - i)
                    break

        if best == INF:
            return -1
        return best + n - 1


s = Solution()
print(s.minOperations([2, 6, 3, 4]))
print(s.minOperations([2, 10, 6, 14]))
