from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        result = nums[0]
        n = len(nums)
        for i in range(1, n):
            result ^= nums[i]
        return result


s = Solution()
print(s.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
print(s.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
