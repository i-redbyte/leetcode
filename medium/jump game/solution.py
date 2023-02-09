from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        j = n
        for i in range(n - 1, -1, -1):
            if j <= i + nums[i]:
                j = i
        return j == 0


s = Solution()
print(s.canJump(nums=[2, 3, 1, 1, 4]))
print(s.canJump(nums=[3, 2, 1, 0, 4]))
