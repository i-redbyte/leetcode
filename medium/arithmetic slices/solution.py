from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        counter = 0
        result = 0
        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                counter += 1
                result = result + counter
            else:
                counter = 0
        return result


s = Solution()
print(s.numberOfArithmeticSlices([1, 2, 3]))
print(s.numberOfArithmeticSlices([1, 2, 3, 4]))
print(s.numberOfArithmeticSlices([1]))
print(s.numberOfArithmeticSlices([-1, -10]))
print(s.numberOfArithmeticSlices([3, -1, -5, -9]))
