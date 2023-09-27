from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums) - 1
        return self.compute(nums, target, 0, n)

    def compute(self, nums: List[int], target: int, start: int, end: int) -> int:
        if start >= end:
            return 0
        if nums[start] + nums[end] < target:
            return (end - start) + self.compute(nums, target, start + 1, end)
        else:
            return self.compute(nums, target, start, end - 1)

    def countPairs1(self, nums: List[int], target: int) -> int:
        result = 0
        nums.sort()
        start = 0
        end = len(nums) - 1
        while start < end:
            if nums[start] + nums[end] < target:
                result += end - start
                start += 1
            else:
                end -= 1
        return result


s = Solution()
print(s.countPairs([-1, 1, 2, 3, 1], target=2))
print(s.countPairs([-6, 2, 5, -2, -7, -1, 3], target=-2))
