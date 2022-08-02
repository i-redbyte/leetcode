from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums) - 1
        for i in range(0, n, 2):
            result = result + ([nums[i+1]] * nums[i])
        return result


s = Solution()
print(s.decompressRLElist([1, 2, 3, 4]))
print(s.decompressRLElist([1, 1, 2, 3]))
