from typing import List


# Kadane's algorithm
# https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = 0
        current_sum = 0
        signed_val = max(nums)
        if signed_val < 0:
            return signed_val
        for i in range(0, n):
            current_sum += nums[i]
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        return max_sum


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(s.maxSubArray([1]))
print(s.maxSubArray([-1]))
print(s.maxSubArray([-1, -2]))
print(s.maxSubArray([5, 4, -1, 7, 8]))
