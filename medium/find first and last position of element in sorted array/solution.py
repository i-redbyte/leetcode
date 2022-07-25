from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = -1
        right = -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                left = mid
            if nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                right = mid
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1

        return [left, right]


s = Solution()
print(s.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
print(s.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))
print(s.searchRange(nums=[], target=0))
print(s.searchRange(nums=[1, 1, 1, 1, 1], target=1))
