from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        mul = 1
        for i in range(n):
            result.append(mul)
            mul *= nums[i]
        mul = 1
        for i in range(n - 1, -1, -1):
            result[i] = result[i] * mul
            mul *= nums[i]
        return result


s = Solution()

print(s.productExceptSelf([1, 2, 3, 4]))
print(s.productExceptSelf([-1, 1, 0, -3, 3]))
