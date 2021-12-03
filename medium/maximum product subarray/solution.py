from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod_max = nums[0]
        prod_min = nums[0]
        result = prod_max
        n = len(nums)
        for i in range(1, n):
            current = nums[i]
            tmp = max(current, prod_max * current, prod_min * current)
            prod_min = min(current, prod_max * current, prod_min * current)
            prod_max = tmp
            result = max(prod_max, result)
        return result


s = Solution()

print(s.maxProduct([2, 3, -2, 4]))
print(s.maxProduct([-2, 0, -1]))
