from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[-(k % len(nums)):] + nums[:-(k % len(nums))]


s = Solution()
s.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3)
