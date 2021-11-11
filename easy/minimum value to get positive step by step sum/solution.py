from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        result = 0
        s = 0
        for i in nums:
            s += i
            result = min(result, s)
        return -result + 1


s = Solution()
print(s.minStartValue([-3, 2, -3, 4, 2]))
print(s.minStartValue([1, 2]))
print(s.minStartValue([1, -2, -3]))
