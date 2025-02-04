from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = current_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                current_sum = nums[i]
            result = max(result, current_sum)
        return result


s = Solution()
print(s.maxAscendingSum([10, 20, 30, 5, 10, 50]))
print(s.maxAscendingSum([10, 20, 30, 40, 50]))
print(s.maxAscendingSum([12, 17, 15, 13, 10, 11, 12]))
print(s.maxAscendingSum([100, 10, 1]))
print(s.maxAscendingSum([3, 6, 10, 1, 8, 9, 9, 8, 9]))
