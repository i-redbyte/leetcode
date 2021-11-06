from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        tmp = 0
        x = 0
        y = 0
        for i in nums:
            tmp ^= i
        p = 1
        while tmp & p == 0:
            p = p << 1
        for i in nums:
            if i & p == 0:
                x ^= i
            else:
                y ^= i
        return [x, y]


s = Solution()
print(s.singleNumber([1, 2, 1, 3, 2, 5]))
print(s.singleNumber([-1, 0]))
print(s.singleNumber([0, 1]))
print(s.singleNumber([2, 2, 33, 33, 17, -100]))
print(s.singleNumber([0, -1, 0, -1, 23, 666, -6, -99999, 3456, -6, -99999, 3456]))
