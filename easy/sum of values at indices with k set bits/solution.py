from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        result = 0
        n = len(nums)
        for i in range(n):
            x = 0
            tmp = i
            while tmp:
                x += tmp & 1
                tmp >>= 1
            if x == k:
                result += nums[i]
        return result


s = Solution()
print(s.sumIndicesWithKSetBits(nums=[5, 10, 1, 5, 2], k=1))
print(s.sumIndicesWithKSetBits(nums=[4, 3, 2, 1], k=2))
