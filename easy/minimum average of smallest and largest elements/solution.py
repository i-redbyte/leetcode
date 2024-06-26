from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)
        half_n = n // 2
        result = []
        for i in range(half_n):
            result.append((nums[i] + nums[n - i - 1]) / 2)
        return min(result)


s = Solution()
print(s.minimumAverage([7, 8, 3, 4, 15, 13, 4, 1]))
print(s.minimumAverage([1, 9, 8, 3, 10, 5]))
print(s.minimumAverage([1, 2, 3, 7, 8, 9]))
