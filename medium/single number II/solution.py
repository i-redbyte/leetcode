from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a, b = 0, 0
        for i in nums:
            c = b & i
            b = b | (a & i)
            a = a ^ i
            b = b & ~c
            a = a & ~c
        return a


s = Solution()
print(s.singleNumber([2, 2, 3, 2]))
print(s.singleNumber([0, 1, 0, 1, 0, 1, 99]))
print(s.singleNumber([30000, 500, 100, 30000, 100, 30000, 100]))
