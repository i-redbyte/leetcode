from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for k in range(1, 4):
            for i in range(len(nums) - k):
                if nums[i] == nums[i + k]:
                    return nums[i]
        return -1


s = Solution()
print(s.repeatedNTimes([1, 2, 3, 3]))
print(s.repeatedNTimes([2, 1, 2, 5, 3, 2]))
print(s.repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]))
