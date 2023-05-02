from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        mul = 1
        for i in nums:
            mul *= i
        if mul > 0:
            return 1
        elif mul == 0:
            return 0
        return -1


s = Solution()
print(s.arraySign([-1, -2, -3, -4, 3, 2, 1]))
print(s.arraySign([1, 5, 0, 2, -3]))
print(s.arraySign([-1, 1, -1, 1, -1]))
