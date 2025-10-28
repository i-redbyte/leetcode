from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        result = 0
        prefix = 0
        suffix = sum(nums)
        for num in nums:
            suffix -= num
            prefix += num
            if num > 0:
                continue
            if prefix == suffix:
                result += 2
            if abs(prefix - suffix) == 1:
                result += 1
        return result


s = Solution()
print(s.countValidSelections([1, 0, 2, 0, 3]))
print(s.countValidSelections([2, 3, 4, 0, 4, 1, 0]))
