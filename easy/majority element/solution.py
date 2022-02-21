from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) < 3:
            return max(nums)
        half = n // 2
        nums.sort()
        return nums[half]


print(Solution().majorityElement([3, 2, 3]))
print(Solution().majorityElement([3, 3, 4]))
print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
