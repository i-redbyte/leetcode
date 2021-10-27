from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        tmp = left
        while tmp <= right:
            if nums[tmp] == 0:
                nums[left], nums[tmp] = nums[tmp], nums[left]
                left += 1
                tmp += 1
            elif nums[tmp] == 1:
                tmp += 1
            else:
                nums[right], nums[tmp] = nums[tmp], nums[right]
                right -= 1
        print(nums)  # for test


s = Solution()
s.sortColors([2, 0, 2, 1, 1, 0])
s.sortColors([2, 0, 1])
s.sortColors([0])
s.sortColors([1])
