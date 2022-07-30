from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums


s = Solution()
print(s.getConcatenation([1, 2, 1]))
print(s.getConcatenation([1, 3, 2, 1]))
