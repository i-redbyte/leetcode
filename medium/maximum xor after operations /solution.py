from typing import List


class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            result |= i
        return result


s = Solution()
print(s.maximumXOR([3, 2, 4, 6]))
print(s.maximumXOR([1, 2, 3, 9, 2]))
