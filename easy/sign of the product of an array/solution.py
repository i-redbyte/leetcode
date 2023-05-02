from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg = 1
        for i in nums:
            if i == 0:
                return 0
            if i < 0:
                neg = -1 * neg
        return neg

    def arraySign2(self, nums: List[int]) -> int:
        neg = 0
        for i in nums:
            if i == 0:
                return 0
            if i < 0:
                neg += 1
        return -1 if (neg % 2 != 0) else 1

    def arraySign1(self, nums: List[int]) -> int:
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
