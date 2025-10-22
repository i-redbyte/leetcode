from typing import List
from collections import Counter


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        if not nums:
            return 0

        a = sorted(nums)
        n = len(a)
        freq = Counter(a)

        cand = set()
        for v in freq.keys():
            cand.add(v)
            cand.add(v - k)
            cand.add(v + k)
        cand = sorted(cand)

        result = 1
        l = r = 0

        for x in cand:
            left = x - k
            right = x + k
            while l < n and a[l] < left:
                l += 1
            while r < n and a[r] <= right:
                r += 1

            in_range = r - l
            equal = freq.get(x, 0)
            result = max(result, min(in_range, equal + numOperations))

        return result


s = Solution()
print(s.maxFrequency(nums=[1, 4, 5], k=1, numOperations=2))
print(s.maxFrequency(nums=[5, 11, 20, 20], k=5, numOperations=1))
