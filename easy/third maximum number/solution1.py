from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = len(nums)
        max1 = max(nums)
        if n < 3:
            return max1
        max2 = self.control_max(nums, max1)
        max3 = self.control_max(nums, max2)

        if max3 == -1 or max3 == max2:
            return max1
        return max3

    def control_max(self, nums: List[int], control_maximum: int) -> int:
        max_value = min(nums)
        for i in nums:
            if max_value < i < control_maximum:
                max_value = i
        return max_value


s = Solution()
print(s.thirdMax([3, 2, 1]))
print(s.thirdMax([1, 2]))
print(s.thirdMax([2, 2, 3, 1]))
print(s.thirdMax([1, 2, 3, 4, 5]))
print(s.thirdMax([6, 4, 5, 7]))
print(s.thirdMax([1, 2, -2147483648]))
