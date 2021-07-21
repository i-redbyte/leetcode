from typing import List

from urllib3.connectionpool import xrange


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        i = 0
        for k in xrange(len(nums)):
            if nums[k] != nums[i]:
                nums[i + 1] = nums[k]
                i += 1
        return i + 1


s = Solution()
print(s.removeDuplicates([1, 1, 2]))
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
