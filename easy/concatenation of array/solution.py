from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        m = 2 * n
        result = [0] * m
        for i, v in enumerate(nums):
            result[i] = v
            result[n + i] = v
        return result

    def getConcatenation1(self, nums: List[int]) -> List[int]:
        return nums + nums


s = Solution()
print(s.getConcatenation([1, 2, 1]))
print(s.getConcatenation([1, 3, 2, 1]))
