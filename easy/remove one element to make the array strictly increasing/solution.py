from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        i = 1
        while i < n and count < 2:
            if nums[i - 1] >= nums[i]:
                count += 1
                if i > 1 and nums[i - 2] >= nums[i]:
                    nums[i] = nums[i - 1]
            i += 1
        return count < 2


s = Solution()
print(s.canBeIncreasing([1, 2, 10, 5, 7]))
print(s.canBeIncreasing([2, 3, 1, 2]))
print(s.canBeIncreasing([1, 1, 1]))
