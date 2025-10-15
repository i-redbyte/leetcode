from typing import List


class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            if n & 1 == 0:
                result |= n
        return result


s = Solution()
print(s.evenNumberBitwiseORs([1, 2, 3, 4, 5, 6]))
print(s.evenNumberBitwiseORs([7, 9, 11]))
print(s.evenNumberBitwiseORs([1, 8, 16]))
