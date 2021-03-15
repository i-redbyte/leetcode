import math
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = set()
        for x in nums:
            if target - x in s:
                first_index = nums.index(target - x)
                nums[first_index] = math.inf
                return [first_index, nums.index(x)]
            s.add(x)


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([3, 2, 4], 6))
print(s.twoSum([3, 3], 6))
