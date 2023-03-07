from functools import reduce
from typing import List


def fold(f, l, a):
    return a if (len(l) == 0) else fold(f, l[1:], f(a, l[0]))


class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        return fold(lambda a, b: a | b, nums, 0)

    def maximumXOR2(self, nums: List[int]) -> int:
        return reduce(lambda a, b: a | b, nums)

    def maximumXOR1(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            result |= i
        return result


s = Solution()
print(s.maximumXOR([3, 2, 4, 6]))
print(s.maximumXOR([1, 2, 3, 9, 2]))
