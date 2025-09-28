from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums) - 3
        for i in range(n, -1, -1):
            if nums[i] + nums[i + 1] > nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0


s = Solution()
print(s.largestPerimeter([2, 1, 2]))
print(s.largestPerimeter([1, 2, 1, 10]))
