from typing import List, Tuple


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        def adjusted_sum(nums: List[int]) -> Tuple[int, int]:
            zeros = nums.count(0)
            return sum(nums) + zeros, zeros

        sum1, zero1 = adjusted_sum(nums1)
        sum2, zero2 = adjusted_sum(nums2)

        if (zero1 == 0 and sum2 > sum1) or (zero2 == 0 and sum1 > sum2):
            return -1

        return max(sum1, sum2)

s = Solution()
print(s.minSum(nums1=[3, 2, 0, 1, 0], nums2=[6, 5, 0]))
print(s.minSum(nums1=[2, 0, 2, 0], nums2=[1, 4]))
print(s.minSum(nums1=[0,29,5,22,5,9,30,11,20,0,18,16,26,11,3,0,24,24,14,24], nums2=[30,12,16,3,24,6,13,0,16]))
