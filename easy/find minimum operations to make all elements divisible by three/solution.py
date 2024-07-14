from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            if i % 3 != 0:
                result += 1
        return result

    def minimumOperations1(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            result += min(3 - (i % 3), i % 3)
        return result


s = Solution()
print(s.minimumOperations([1, 2, 3, 4]))
print(s.minimumOperations([3, 6, 9]))
