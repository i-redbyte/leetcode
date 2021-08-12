from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        result = self.binarySearch(nums, target)
        if result == -1:
            n = len(nums)
            if target > max(nums):
                return n
            elif target < min(nums):
                return 0
            for i in range(n):
                if target < nums[i]:
                    return i
        return result

    def binarySearch(self, nums: List[int], target: int):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


s = Solution()
print(s.searchInsert([1, 3, 5, 6], 5))
print(s.searchInsert([1, 3, 5, 6], 2))
print(s.searchInsert([1, 3, 5, 6], 7))
print(s.searchInsert([1, 3, 5, 6], 0))
print(s.searchInsert([1], 0))
print(s.searchInsert([1, 3, 5, 6], 4))
print(s.searchInsert([1, 3, 5, 6], 1))
print(s.searchInsert([1, 3, 5, 6], 3))
print(s.searchInsert([3, 4, 9, 10], 5))
print(s.searchInsert([3, 6, 7, 8, 10], 5))
