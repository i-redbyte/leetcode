from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % p
        if remainder == 0:
            return 0

        prefix_sum = 0
        min_len = len(nums)
        prefix_mod_map = {0: -1}

        for i, num in enumerate(nums):
            prefix_sum += num
            mod = prefix_sum % p
            target = (mod - remainder) % p
            if target in prefix_mod_map:
                min_len = min(min_len, i - prefix_mod_map[target])
            prefix_mod_map[mod] = i

        return min_len if min_len < len(nums) else -1


s = Solution()
print(s.minSubarray(nums=[3, 1, 4, 2], p=6))
print(s.minSubarray(nums=[6, 3, 5, 2], p=9))
print(s.minSubarray(nums=[1, 2, 3], p=3))
