from collections import defaultdict
from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        dick = defaultdict(int)
        result = 0
        for n in nums:
            dick[n] += 1
            result += dick[n - k] + dick[n + k]
        return result


s = Solution()
print(s.countKDifference([1, 2, 2, 1], k=1))
print(s.countKDifference([1, 3], k=3))
print(s.countKDifference([3, 2, 1, 5, 4], k=2))
