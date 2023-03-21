from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        start = 0
        end = 0
        n = len(nums)
        while end != n:
            if nums[end] != 0:
                end += 1
                start = end
            else:
                result += end - start + 1
                end += 1
        return result

    def zeroFilledSubarray1(self, nums: List[int]) -> int:
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
