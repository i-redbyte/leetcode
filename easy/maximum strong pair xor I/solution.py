from typing import List


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        def isStrongPair(x: int, y: int) -> int:
            return abs(x - y) <= min(x, y)

        max_xor = 0
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if isStrongPair(nums[i], nums[j]):
                    max_xor = max(max_xor, nums[i] ^ nums[j])
        return max_xor


s = Solution()
print(s.maximumStrongPairXor([1, 2, 3, 4, 5]))
print(s.maximumStrongPairXor([10, 100]))
print(s.maximumStrongPairXor([5, 6, 25, 30]))
