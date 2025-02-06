from collections import defaultdict
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = defaultdict(int)

        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_count[product] += 1

        result = 0
        for count in product_count.values():
            if count >= 2:
                pairs = count * (count - 1) // 2
                result += pairs * 8

        return result


s = Solution()
print(s.tupleSameProduct([2, 3, 4, 6]))
print(s.tupleSameProduct([1, 2, 4, 5, 10]))
