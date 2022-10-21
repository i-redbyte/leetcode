from collections import Counter
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        a = Counter(nums)
        result = 0
        for k, v in a.items():
            if v == 1:
                result += k
        return result


s = Solution()
print(s.sumOfUnique([1, 2, 3, 2]))
print(s.sumOfUnique([1, 1, 1, 1, 1]))
print(s.sumOfUnique([1, 2, 3, 4, 5]))
