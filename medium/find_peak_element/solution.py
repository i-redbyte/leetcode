from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            midle = (left + right) // 2
            if nums[midle] > nums[midle + 1]:
                right = midle
            else:
                left = midle + 1
        return left


s = Solution()
print(s.findPeakElement([3, 1, 2]))
print(s.findPeakElement([1, 2, 3]))
print(s.findPeakElement([1]))
print(s.findPeakElement([1, 2, 3, 1]))
print(s.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
