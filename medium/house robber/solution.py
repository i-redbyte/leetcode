from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        intermediate_result = 0
        for i in nums:
            tmp = result
            result = max(i + intermediate_result, result)
            intermediate_result = tmp
        return result


s = Solution()
print(s.rob([1, 2, 3, 1]))
print(s.rob([2, 7, 9, 3, 1]))
