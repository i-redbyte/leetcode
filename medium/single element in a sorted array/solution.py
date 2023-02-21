from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] != nums[mid + 1]:
                right = mid
            else:
                left = mid + 2
        return nums[left]

    def singleNonDuplicate1(self, nums: List[int]) -> int:
        result = nums[0]
        n = len(nums)
        for i in range(1, n):
            result ^= nums[i]
        return result


s = Solution()
print(s.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
print(s.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
