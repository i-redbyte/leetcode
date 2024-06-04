from typing import List


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        result = 0
        s = set()
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    s.add(nums[i])
        if len(s) == 0:
            return result
        for i in s:
            result = result ^ i
        return result


s = Solution()
print(s.duplicateNumbersXOR([1, 2, 1, 3]))
print(s.duplicateNumbersXOR([1, 2, 3]))
print(s.duplicateNumbersXOR([1, 2, 2, 1]))
