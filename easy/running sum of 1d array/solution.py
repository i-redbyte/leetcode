from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i-1]
        return nums


s = Solution()
print(s.runningSum([1, 2, 3, 4]))
print(s.runningSum([1, 1, 1, 1, 1]))
print(s.runningSum([3, 1, 2, 10, 1]))
print(s.runningSum([3, 1]))
