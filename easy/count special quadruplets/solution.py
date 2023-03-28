from collections import defaultdict
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        result = 0
        d = defaultdict(int)
        n = len(nums)
        for i in range(1, n):
            for j in range(0, i):
                d[nums[j] + nums[i]] += 1
            for k in range(i + 2, n):
                result += d[nums[k] - nums[i + 1]]
        return result


s = Solution()
print(s.countQuadruplets([1, 2, 3, 6]))
print(s.countQuadruplets([3, 3, 6, 4, 5]))
print(s.countQuadruplets([1, 1, 1, 3, 5]))
