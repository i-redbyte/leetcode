from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        defects = 0
        n = len(nums) - 1
        for i in range(n):
            if nums[i] > nums[i + 1]:
                defects += 1
        if defects > 1:
            return False

        return defects == 0 or nums[0] >= nums[n]


s = Solution()
print(s.check([3, 4, 5, 1, 2]))
print(s.check([2, 1, 3, 4]))
print(s.check([1, 2, 3]))
print(s.check([6, 10, 6]))
