from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        max_len = 1

        for right in range(n):
            while nums[left] * k < nums[right]:
                left += 1
            max_len = max(max_len, right - left + 1)

        return n - max_len


s = Solution()
print(s.minRemoval(nums=[2, 1, 5], k=2))
print(s.minRemoval(nums=[1, 6, 2, 9], k=3))
print(s.minRemoval(nums=[4, 6], k=2))
