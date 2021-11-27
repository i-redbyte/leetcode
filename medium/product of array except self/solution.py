from typing import List


class Solution:

    def productExceptSelf1(self, nums: List[int]) -> List[int]:
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

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        m = n - 1
        result = [1] * n
        left = 1
        right = 1
        for i in range(n):
            result[i] *= left
            result[m - i] *= right
            left *= nums[i]
            right *= nums[m - i]
        return result


s = Solution()

print(s.productExceptSelf([1, 2, 3, 4]))
print(s.productExceptSelf([-1, 1, 0, -3, 3]))
