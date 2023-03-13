from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums) + 1
        s = set(nums)
        for i in range(1, n):
            if i not in s:
                result.append(i)
        return result


s = Solution()
print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
print(s.findDisappearedNumbers([1, 1]))
