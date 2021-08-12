from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        s = 0
        result = []
        for i in nums:
            s = s * 2 + i
            result.append(s % 5 == 0)
        return result


s = Solution()
print(s.prefixesDivBy5([0, 1, 1]))
print(s.prefixesDivBy5([1, 1, 1]))
print(s.prefixesDivBy5([0, 1, 1, 1, 1, 1]))
print(s.prefixesDivBy5([1, 1, 1, 0, 1]))
