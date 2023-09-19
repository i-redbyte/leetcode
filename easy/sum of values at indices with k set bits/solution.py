from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        if k == 0:
            return nums[0]
        n = len(nums)
        tmp = [0] * n
        result = 0
        for i in range(1, n):
            tmp[i] = 1 + tmp[i & (i - 1)]
            if tmp[i] == k:
                result += nums[i]
        return result

    def sumIndicesWithKSetBits2(self, nums: List[int], k: int) -> int:
        return sum(x for i, x in enumerate(nums) if bin(i).count('1') == k)

    def sumIndicesWithKSetBits1(self, nums: List[int], k: int) -> int:
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
