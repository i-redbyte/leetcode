from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        n = len(nums)
        for i in range(0, n):
            result ^= i ^ nums[i]
        return result

    # with Gauss's Formula; See: https://brilliant.org/wiki/sum-of-n-n2-or-n3/
    def missingNumber2(self, nums: List[int]) -> int:
        k = len(nums) * (len(nums) + 1) // 2
        s = 0
        for i in nums:
            s += i
        return k - s


s = Solution()
print(s.missingNumber([3, 0, 1]))
print(s.missingNumber([0, 1]))
print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(s.missingNumber([0]))
# 2 solution
print("---Two solution!---")
print(s.missingNumber2([3, 0, 1]))
print(s.missingNumber2([0, 1]))
print(s.missingNumber2([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(s.missingNumber2([0]))
