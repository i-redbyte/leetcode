from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        for end in range(n - 1, 0, -1):
            for i in range(end):
                nums[i] = (nums[i] + nums[i + 1]) % 10
        return nums[0]


s = Solution()
print(s.triangularSum([1, 2, 3, 4, 5]))
print(s.triangularSum([5]))
