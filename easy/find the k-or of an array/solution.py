from typing import List


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        result = 0
        for bit_position in range(32):
            count = 0
            for num in nums:
                if num & (1 << bit_position):
                    count += 1

            if count >= k:
                result |= (1 << bit_position)
        return result


s = Solution()
print(s.findKOr(nums=[7, 12, 9, 8, 9, 15], k=4))
print(s.findKOr(nums=[2, 12, 1, 11, 4, 5], k=6))
print(s.findKOr(nums=[10, 8, 5, 9, 11, 6, 8], k=1))
