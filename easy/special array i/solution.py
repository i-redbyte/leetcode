from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        for i in range(n):
            if nums[i] & 1 == nums[i + 1] & 1:
                return False
        return True


s = Solution()
print(s.isArraySpecial([1]))
print(s.isArraySpecial([2, 1, 4]))
print(s.isArraySpecial([4, 3, 1, 6]))
print(s.isArraySpecial([1, 5]))
