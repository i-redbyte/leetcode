from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums) - 1
        return (nums[n] * nums[n - 1]) - (nums[0] * nums[1])


s = Solution()
print(s.maxProductDifference([5, 6, 2, 7, 4]))
print(s.maxProductDifference([4, 2, 5, 9, 7, 4, 8]))
