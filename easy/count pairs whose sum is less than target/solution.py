from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
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
