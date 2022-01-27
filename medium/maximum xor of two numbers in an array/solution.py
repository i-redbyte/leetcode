from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        bin_number_max_len = len(bin(max(nums))) - 2
        result = 0
        for prefix_len in range(1, bin_number_max_len + 1):
            result <<= 1
            current = result | 1
            shift = bin_number_max_len - prefix_len
            prefixes = {n >> shift for n in nums}
            found_match = any(current ^ prefix in prefixes for prefix in prefixes)
            result |= found_match
        return result

    def findMaximumXOR1(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                cond = nums[i] ^ nums[j]
                if cond > result:
                    result = cond
        return result


s = Solution()
print(s.findMaximumXOR([3, 10, 5, 25, 2, 8]))
print(s.findMaximumXOR([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]))
print(s.findMaximumXOR([2,4]))
