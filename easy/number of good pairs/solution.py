from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    result += 1
        return result


s = Solution()
print(s.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
print(s.numIdenticalPairs([1, 1, 1, 1]))
print(s.numIdenticalPairs([1, 2, 3]))
