from functools import reduce
from typing import List


class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        result = 0
        for i in nums:
            result = result ^ i
        return result == 0 or len(nums) & 1 == 0

    def xorGame1(self, nums: List[int]) -> bool:
        return reduce(lambda a, b: a ^ b, nums) == 0 or len(nums) & 1 == 0


s = Solution()
print(s.xorGame([1, 1, 2]))
print(s.xorGame([0, 1]))
print(s.xorGame([1, 2, 3]))
