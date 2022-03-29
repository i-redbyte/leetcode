from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        result = 0
        m = len(nums)
        n = m - 1
        bits = n.bit_length()
        for bit in range(bits):
            mask = 1 << bit
            base_count = 0
            nums_count = 0
            for i in range(m):
                if i & mask:
                    base_count += 1
                if nums[i] & mask:
                    nums_count += 1
            if nums_count - base_count > 0:
                result |= mask
        return result


print(Solution().findDuplicate([1, 3, 4, 2, 2]))
print(Solution().findDuplicate([3, 1, 3, 4, 2]))
print(Solution().findDuplicate([1, 2, 3, 5, 5, 4]))
print(Solution().findDuplicate([2, 2, 2, 2, 2, 2]))
