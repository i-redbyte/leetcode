from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        end = 0
        start = 0
        for i in range(n - 1):
            start = max(start, i + nums[i])
            if i == end:
                result += 1
                end = start
        return result


s = Solution()
print(s.jump(nums=[2, 3, 1, 1, 4]))
print(s.jump(nums=[2, 3, 0, 1, 4]))
