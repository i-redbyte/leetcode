from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor_result = 0
        if len(nums2) & 1 == 1:
            for num in nums1:
                xor_result ^= num
        if len(nums1) & 1 == 1:
            for num in nums2:
                xor_result ^= num
        return xor_result


s = Solution()
print(s.xorAllNums(nums1=[2, 1, 3], nums2=[10, 2, 5, 0]))
print(s.xorAllNums(nums1=[1, 2], nums2=[3, 4]))
