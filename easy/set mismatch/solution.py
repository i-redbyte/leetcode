from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = 0
        missing = 0
        n = len(nums)
        for i in nums:
            nums[i % n - 1] += n
        for i, v in enumerate(nums):
            if v <= n:
                missing = i + 1
            elif v > 2 * n:
                duplicate = i + 1
            if duplicate and missing:
                return [duplicate, missing]


s = Solution()
print(s.findErrorNums([1, 2, 2, 4]))
print(s.findErrorNums([1, 1]))
print(s.findErrorNums([1, 1, 3]))
print(s.findErrorNums([1, 1, 3, 4]))
print(s.findErrorNums([1, 2, 3, 4, 5, 5]))
