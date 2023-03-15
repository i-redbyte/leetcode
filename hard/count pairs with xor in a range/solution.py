from collections import Counter
from typing import List


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        return self.xorPairs(nums, high + 1) - self.xorPairs(nums, low)

    def xorPairs(self, nums: List[int], high: int) -> int:
        res = 0
        for k in range(31, -1, -1):
            target = high >> k
            if target & 1 == 0:
                continue
            target -= 1
            counter = Counter(num >> k for num in nums)
            for mask in counter:
                res += counter[mask] * counter[target ^ mask]
                if mask == target ^ mask:
                    res -= counter[mask]
        return res // 2


s = Solution()
print(s.countPairs(nums=[1, 4, 2, 7], low=2, high=6))
print(s.countPairs(nums=[9, 8, 4, 2, 1], low=5, high=14))
