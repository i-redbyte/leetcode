from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        n = len(nums)
        for i in range(0, n):
            result ^= i ^ nums[i]
        return result


s = Solution()
print(s.missingNumber([3, 0, 1]))
print(s.missingNumber([0, 1]))
print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(s.missingNumber([0]))
