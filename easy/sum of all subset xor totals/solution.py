from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        n = len(nums) - 1
        for i in nums:
            result |= i
        return result * pow(2, n)


s = Solution()
print(s.subsetXORSum([1, 3]))
print(s.subsetXORSum([5, 1, 6]))
print(s.subsetXORSum([3, 4, 5, 6, 7, 8]))
