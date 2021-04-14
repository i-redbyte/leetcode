from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = max2 = max3 = min(nums)
        for i in set(nums):
            if i > max1:
                max3, max2 = max2, max3
                max1, max2 = i, max1
            elif i > max2:
                max2, max3 = i, max2
            elif i > max3:
                max3 = i
        if len(set(nums)) < 3:
            return max1
        return max3


s = Solution()
print(s.thirdMax([3, 2, 1]))
print(s.thirdMax([1, 2]))
print(s.thirdMax([2, 2, 3, 1]))
print(s.thirdMax([1, 2, 3, 4, 5]))
print(s.thirdMax([6, 4, 5, 7]))
print(s.thirdMax([1, 2, -2147483648]))
