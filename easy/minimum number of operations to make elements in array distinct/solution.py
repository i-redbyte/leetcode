from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        mask = 0
        n = len(nums)
        for i in reversed(range(n)):
            mask ^= 1 << nums[i]
            if mask & (1 << nums[i]) == 0:
                return (i + 3) // 3
        return 0


s = Solution()
print(s.minimumOperations([1, 2, 3, 4, 2, 3, 3, 5, 7]))
print(s.minimumOperations([4, 5, 6, 4, 4]))
print(s.minimumOperations([6, 7, 8, 9]))
