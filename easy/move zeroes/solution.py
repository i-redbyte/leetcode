from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNotZero = 0
        for (i, v) in enumerate(nums):
            if v != 0:
                nums[lastNotZero], nums[i] = nums[i], nums[lastNotZero]
                lastNotZero += 1


Solution().moveZeroes([0, 1, 0, 3, 12])
