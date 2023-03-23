from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums) - 1
        result = []
        xor = 0
        maximus = pow(2, maximumBit) - 1
        for i in nums:
            xor ^= i
        for i in range(n, -1, -1):
            result.append(xor ^ maximus)
            xor ^= nums[i]
        return result


s = Solution()
print(s.getMaximumXor(nums=[0, 1, 1, 3], maximumBit=2))
print(s.getMaximumXor(nums=[2, 3, 4, 7], maximumBit=3))
print(s.getMaximumXor(nums=[0, 1, 2, 2, 5, 7], maximumBit=3))
