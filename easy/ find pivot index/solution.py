from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        left_sum = 0
        for i, n in enumerate(nums):
            if left_sum == (s - left_sum - n):
                return i
            left_sum += n
        return -1


s = Solution()
print(s.pivotIndex([1, 7, 3, 6, 5, 6]))
print(s.pivotIndex([1, 2, 3]))
print(s.pivotIndex([2, 1, -1]))
