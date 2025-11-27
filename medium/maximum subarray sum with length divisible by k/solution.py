from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        min_pref = {0: 0}
        pref = 0
        result = None

        for i, x in enumerate(nums, start=1):
            pref += x
            mod = i % k

            if mod in min_pref:
                candidate = pref - min_pref[mod]
                if result is None or candidate > result:
                    result = candidate

                if pref < min_pref[mod]:
                    min_pref[mod] = pref
            else:
                min_pref[mod] = pref

        return result if result is not None else 0


s = Solution()
print(s.maxSubarraySum(nums=[1, 2], k=1))
print(s.maxSubarraySum([-1, -2, -3, -4, -5], k=4))
print(s.maxSubarraySum([-5, 1, 2, -3, 4], k=2))
