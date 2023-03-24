from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result = 0
        n = len(nums) - 1
        for i in range(n):
            if nums[i] >= nums[i + 1]:
                result += nums[i] - nums[i + 1] + 1
                nums[i + 1] = nums[i] + 1
            else:
                result += 0
        return result


s = Solution()
print(s.minOperations([1, 1, 1]))
print(s.minOperations([1, 5, 2, 4, 1]))
print(s.minOperations([8]))
