from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if 2 * k > n:
            return False
        if k == 1:
            return n >= 2

        good = [1 if nums[i] < nums[i + 1] else 0 for i in range(n - 1)]
        pref = [0]
        for x in good:
            pref.append(pref[-1] + x)

        def sum_range(l: int, r: int) -> int:
            return pref[r + 1] - pref[l]

        for a in range(0, n - 2 * k + 1):
            if sum_range(a, a + k - 2) == k - 1 and sum_range(a + k, a + 2 * k - 2) == k - 1:
                return True
        return False


s = Solution()
print(s.hasIncreasingSubarrays(nums=[2, 5, 7, 8, 9, 2, 3, 4, 3, 1], k=3))
print(s.hasIncreasingSubarrays(nums=[1, 2, 3, 4, 4, 4, 4, 5, 6, 7], k=5))
