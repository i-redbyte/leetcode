from typing import List


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def get_cost(base):
            return sum(abs(base - num) * c for num, c in zip(nums, cost))

        start, end = min(nums), max(nums)
        result = get_cost(nums[0])
        while start < end:
            mid = (start + end) // 2
            c1 = get_cost(mid)
            c2 = get_cost(mid + 1)
            result = min(c1, c2)
            if c1 > c2:
                start = mid + 1
            else:
                end = mid
        return result


s = Solution()
print(s.minCost(nums=[1, 3, 5, 2], cost=[2, 3, 1, 14]))
print(s.minCost(nums=[2, 2, 2, 2, 2], cost=[4, 2, 8, 1, 3]))
