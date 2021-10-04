from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i in nums:
            if i & 1 == 0:
                result.insert(0, i)
            else:
                result.insert(n, i)
        return result


s = Solution()
print(s.sortArrayByParity([3, 1, 2, 4]))
print(s.sortArrayByParity([0]))
