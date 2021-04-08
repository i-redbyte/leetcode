from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        bit_set = 0
        for i in nums:
            if 0 < i < 301:
                bit_set |= (1 << i)

        for i in range(1, 301):
            if bit_set & (1 << i) == 0:
                return i


s = Solution()

print(s.firstMissingPositive([1, 2, 0]))
print(s.firstMissingPositive([3, 4, -1, 1]))
print(s.firstMissingPositive([7, 8, 9, 11, 12]))
