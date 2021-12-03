from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = prod_min = prod_max = nums[0]
        for n in nums[1:]:
            prod_min, prod_max = min(n, prod_min * n, prod_max * n), max(n, prod_min * n, prod_max * n)
            if prod_max > result:
                result = prod_max
        return result

    def maxProduct1(self, nums: List[int]) -> int:
        prod_max = prod_min = result = nums[0]
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
