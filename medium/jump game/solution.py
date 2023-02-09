from typing import List


class Solution:
    def solution(self, nums: List[int], x: int) -> bool:
        n = len(nums) - 1
        if x == n:
            return True
        if x >= n+1 or nums[x] == 0:
            return False
        result = False
        for i in range(1, nums[x]+1):
            result = result or self.solution(nums, x + i)
        return result

    def canJump(self, nums: List[int]) -> bool:
        return self.solution(nums, 0)

    def canJump1(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        j = n
        for i in range(n, -1, -1):
            if j <= i + nums[i]:
                j = i
        return j == 0


s = Solution()
print(s.canJump(nums=[2, 3, 1, 1, 4]))
print(s.canJump(nums=[3, 2, 1, 0, 4]))
