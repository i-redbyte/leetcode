from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        result = original
        while result in nums:
            result *= 2
        return result


s = Solution()
print(s.findFinalValue(nums=[5, 3, 6, 1, 12], original=3))
print(s.findFinalValue(nums=[2, 7, 9], original=4))
