from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        sub_array = 0
        for i in nums:
            if i == 0:
                sub_array += 1
            else:
                sub_array = 0
            result += sub_array
        return result


s = Solution()
print(s.zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]))
print(s.zeroFilledSubarray([0, 0, 0, 2, 0, 0]))
print(s.zeroFilledSubarray([2, 10, 2019]))
