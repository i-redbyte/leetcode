from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = 0
        for i in range(k):
            s += nums[i]
        maxSum = s
        n = len(nums)
        for i in range(k, n):
            s = s - nums[i - k] + nums[i]
            maxSum = max(maxSum, s)
        return maxSum / k


s = Solution()
print(s.findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4))
print(s.findMaxAverage(nums=[5], k=1))
