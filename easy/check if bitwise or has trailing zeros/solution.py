from typing import List


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        result = 0
        for i in nums:
            if i & 1 == 0:
                result += 1
            if result > 1:
                return True
        return False


s = Solution()
print(s.hasTrailingZeros([1, 2, 3, 4, 5]))
print(s.hasTrailingZeros([2, 4, 8, 16]))
print(s.hasTrailingZeros([1, 3, 5, 7, 9]))
print(s.hasTrailingZeros([1, 2]))
