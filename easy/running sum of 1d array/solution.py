from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            result.append(result[i - 1] + nums[i])
        return result


s = Solution()
print(s.runningSum([1, 2, 3, 4]))
print(s.runningSum([1, 1, 1, 1, 1]))
print(s.runningSum([3, 1, 2, 10, 1]))
print(s.runningSum([3, 1]))
