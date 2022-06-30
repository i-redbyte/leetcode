from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        a = sorted(nums)
        mid = len(nums) // 2
        medium = a[mid]
        result = 0
        for i in a:
            result += abs(i - medium)
        return result


s = Solution()
print(s.minMoves2([1, 2, 3]))
print(s.minMoves2([1, 10, 2, 9]))
print(s.minMoves2([1, 1, 1, 1]))
print(s.minMoves2([9, 5, 1, 5]))
