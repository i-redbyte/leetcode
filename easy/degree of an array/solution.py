from collections import defaultdict
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for i, x in enumerate(nums):
            d[x].append(i)
        m = max([len(v) for v in d.values()])
        result = len(nums)
        for v in d.values():
            if len(v) == m:
                result = min(result, v[-1] - v[0] + 1)
        return result


s = Solution()
print(s.findShortestSubArray([1, 2, 2, 3, 1]))
print(s.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))
