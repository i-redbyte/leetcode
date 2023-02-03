from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s1 = sum(nums)
        s2 = 0
        for i in nums:
            s2 += self.digital_root(i)
        return abs(s1 - s2)

    def digital_root(self, n: int):
        result = 0
        while n > 0:
            result += n % 10
            n = n // 10
        return result


s = Solution()
print(s.differenceOfSum([1, 15, 6, 3]))
print(s.differenceOfSum([1, 2, 3, 4]))
