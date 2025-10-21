from typing import List
import collections


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        count = collections.Counter(nums)
        line = {}
        candidates = set()
        for x in nums:
            line[x - k] = line.get(x - k, 0) + 1
            line[x + k + 1] = line.get(x + k + 1, 0) - 1
            candidates.add(x)
            candidates.add(x - k)
            candidates.add(x + k + 1)

        adjustable = 0
        result = 0
        for v in sorted(candidates):
            adjustable += line.get(v, 0)
            eq = count.get(v, 0)
            can_adjust_others = adjustable - eq
            result = max(result, eq + min(numOperations, can_adjust_others))

        return result


s = Solution()
print(s.maxFrequency(nums=[1, 4, 5], k=1, numOperations=2))
print(s.maxFrequency(nums=[5, 11, 20, 20], k=5, numOperations=1))
